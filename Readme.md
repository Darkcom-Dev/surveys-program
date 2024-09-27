Surveys program
===
Version 0.05

Hybrid combination between Dane surveys and Sisben surveys.<br> 
In Colombia DANE is the national department of statistics that obtain information pf the civil population and your live quality. 
Sisben is a beneficiary program for poor families, for give subsides.<br>

My intension is create a combination of this surveys and give a grade if deserve a subside in Colombia, 
but the final reason is auto learning and expanding portfolio.<br>

[https://darkcom-dev.github.io/surveys-program/](Project webpage)

## How to install
1. Make sure you have installed Python 3.9 or earlier.
2. Clone this repository.
3. Install dependencies in `requirements.txt`

Know Issues
---

- [x] Get info from entries generated from loop in home window.
- [x] Get formated date in persons_ui.
- [ ] Get formated direction in dwelling basic.
- [ ] Enhance ttk_utils to simplify code.
- [ ] Evaluate if use interface for "Next ▶" button.
- [ ] Create "Pause" button.

Persons
- [x] born_date change the year each time that modify the calendar
- [x] born_date not calculate user age
- [ ] Persons class save data in save_ui
- [x] Active ethnicity Top Level
- [x] Established connection with health_ui
Save_ui
- [x] Get today date from datetime module

Log
---
- Enhance in persons_ui.py
- Data validations in persons_ui
- Separation of Ethnicity of persons_ui.py
- Enhance of ttk_utils.py
