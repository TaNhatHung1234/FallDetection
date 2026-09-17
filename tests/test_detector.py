# tests/test_detector.py

from src.detector import PersonDetector

def test_person_label():
    detector = PersonDetector()

    assert detector.is_person("person") == True