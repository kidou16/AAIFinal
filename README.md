# Applied Artificial Intelligence 2025/2026
## Final Exam: COMPAS Case Study

**Lecturer**: Prof. Niklas Kühl<br>
**Supervisors**: Luca Deck, Victor Kolominsky-Rabas<br>
**Submission Due Date**: Sunday, February 8th 2026

---
### Submission

- Please submit your code in GitLab.
- Update the ``requirements.txt`` if you use additional packages.
- Export and upload all final model versions **used for the deployment task** that you trained yourself and took more than a minute to train.
- Describe all plots and explain your reasoning for all performance evaluations.
- Make sure to document your approach, to make it easier to understand the code. However, if you write extensive paragraphs of comments, we will delete / shorten them for the oral exam!

### Setup

**Create a virtual environment in VS Code**:
- Open VS Code and navigate to your project directory.
- Press `Ctrl+Shift+P` to open the command palette.
- Type `Python: Select Interpreter`
- Select `Create Virtual Environment`
- Select `Venv`
- Select a Python Interpretation (version ~ 3.11.x)
- Select `requirements.txt` to install necessary packages. 
<br>
You are allowed to install and use other packages, if you want to. Make sure you are able to explain all code that you include in your solution.

### General Background:

![Logo](figures/Northpointe.png)
<br>
The COMPAS software, developed by Northpointe, is a commercial risk assessment tool used by courts and correctional facilities to estimate a criminal defendant's likelihood of re-offending (*recidivism*). Judges and parole officers often consult these scores when making decisions about bail, sentencing, and probation.
Because these scores can decide the fates of US citizens, COMPAS is a popular example for high-risk AI systems and has been thoroughly scrutinized by investigative journalists from ProPublica. You can find more information on this case by looking into their [article](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing), their [published analysis](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm), and their [code](https://github.com/propublica/compas-analysis).

Your task is to replicate the critical analysis from the investigative journalists by leveraging methodology from the Applied AI course. Based on the insights from this critical analysis, you design a human-AI interaction that limits ethical and societal risks.