# Technical Research Paper: Deceptive Opportunity Detector

## 1. Problem
Students in Iraq get fake job emails like Unibase asking passport + $200 fee + crypto wallet before interview. VirusTotal only checks links, not psychological manipulation.

## 2. Methodology
Collected 8 anonymized samples, extracted patterns: fee before invitation, guaranteed visa, crypto wallet, urgent payment. Built Python function check_email() with scoring: 2+ indicators = SCAM.

## 3. Architecture
Input text -> Preprocess -> Pattern extractor -> Scoring engine -> Explainable output with reasons

## 4. Results
Flagged Unibase type 3/3, GulfTalent fake 2/2, Failed on 1 clean-language sample that needs BERT

## 5. Ethics
Transparency (shows why), Protection of vulnerable students, Accountability (warns not deletes)

## 6. Future
Add BERT, WHOIS check, Gmail API, Arabic support
