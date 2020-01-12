"""
This file contains CVParser class based on
ResumeParser from pyresparser package
https://github.com/OmkarPathak/pyresparser/tree/master/pyresparser

It was simplified to extract only skills.
It faster then original ResumeParser class.

Besides cutting unused functions i modified extract_skills function
(https://github.com/OmkarPathak/pyresparser/blob/master/pyresparser/utils.py)
to filter verbs from extracted skills and
get more relevant results.

"""

import io
import os
import pandas as pd
import pyresparser
import spacy

from pyresparser.utils import extract_text


class CVParser:
    """
    Class for extracting skills from .pdf, .doc, .docx
    files using spacy nlp library
    """
    def __init__(
        self,
        resume,
        skills_file=None,
    ):
        nlp = spacy.load('en_core_web_sm')
        self.__skills_file = skills_file
        self.__details = {
            'name': None,
            'email': None,
            'mobile_number': None,
            'skills': None,
            'college_name': None,
            'degree': None,
            'designation': None,
            'experience': None,
            'company_names': None,
            'no_of_pages': None,
            'total_experience': None,
        }
        self.__resume = resume
        if not isinstance(self.__resume, io.BytesIO):
            ext = os.path.splitext(self.__resume)[1].split('.')[1]
        else:
            ext = self.__resume.name.split('.')[1]
        self.__text_raw = extract_text(self.__resume, '.' + ext)
        self.__text = ' '.join(self.__text_raw.split())
        self.__nlp = nlp(self.__text)
        self.__noun_chunks = list(self.__nlp.noun_chunks)
        if not skills_file:
            module_path = os.path.dirname(pyresparser.__file__)
            skills_file_name = 'skills.csv'
            self.__skills_file = os.path.join(module_path, skills_file_name)

    def extract_skills(self):
        """
        method for extracting skills from spacy nlp text
        :return: list[str] list of skills extracted
        """
        # get provided skills list
        data = pd.read_csv(self.__skills_file)
        skills = list(data.columns.values)

        skillset = []

        # one-grams tokens
        one_gram_tokens = [token.text.lower() for token in self.__nlp
                           if not (token.is_stop or token.pos_ == 'VERB')]

        for token in one_gram_tokens:
            if token in skills:
                skillset.append(token)

        # bi-grams and tri-grams
        bi_tri_gram_tokens = [token.text.lower().strip()
                              for token in self.__noun_chunks]

        for token in bi_tri_gram_tokens:
            if token in skills:
                skillset.append(token)

        return [i.capitalize() for i in set(skillset)]
