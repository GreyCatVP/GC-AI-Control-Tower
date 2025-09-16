from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def redact_inline(text: str) -> str:
    results = analyzer.analyze(text=text, language="ru")
    return anonymizer.anonymize(text=text, analyzer_results=results).text
