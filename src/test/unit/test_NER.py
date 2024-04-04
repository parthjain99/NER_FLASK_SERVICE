import pytest
from src.services.NER_service import ner_spacy

def test_ner_spacy_empty_text():
    text = ""
    expected_entities = {"error": "Invalid input"}
    assert ner_spacy(text) == expected_entities

def test_ner_spacy_no_entities():
    text = "This is a sample text."
    expected_entities = {}
    assert ner_spacy(text) == expected_entities

def test_ner_spacy_single_entity():
    text = "Apple Inc. is a technology company."
    expected_entities = {0: {'text': 'Apple Inc.', 'label': 'ORG', 'start_char': 0, 'end_char': 10}}
    assert ner_spacy(text) == expected_entities

def test_ner_spacy_multiple_entities():
    text = "Microsoft Corporation is located in Redmond, Washington."
    expected_entities = {
        0: {'text': 'Microsoft Corporation', 'label': 'ORG', 'start_char': 0, 'end_char': 21},
        1: {'text': 'Redmond', 'label': 'GPE', 'start_char': 36, 'end_char': 43},
        2: {'text': 'Washington', 'label': 'GPE', 'start_char': 45, 'end_char': 55}
    }
    assert ner_spacy(text) == expected_entities

def test_ner_spacy_overlapping_entities():
    text = "New York City is a city in New York state."
    expected_entities = {
        0: {'text': 'New York City', 'label': 'GPE', 'start_char': 0, 'end_char': 13},
        1: {'text': 'New York', 'label': 'GPE', 'start_char': 27, 'end_char': 35}
    }
    assert ner_spacy(text) == expected_entities
