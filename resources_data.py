"""
Per-WEEK learning resources for the CHEF_P Roadmap Tracker.

Keyed by each week's focus name (the same names used in CURRICULUM in app.py).
Every entry is (type, label, url). Types:
  video  - YouTube video / playlist / channel
  course - structured course (free unless noted)
  book   - book (free unless the label says "paid")
  paper  - research paper
  repo   - GitHub repository
  doc    - documentation, blog post, or tutorial
  note   - a suggested proof-of-work exercise (no link)
"""

# ---- reusable links (defined once so a typo can't make two weeks disagree) ----
YT = "https://www.youtube.com"
B3B_LINALG = YT + "/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab"
B3B_CALC = YT + "/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr"
B3B_NN = YT + "/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi"
B3B_PROB = YT + "/playlist?list=PLiAulSm0XXgvCGe63mrAkda9UQ9478YQv"
SQ_ML = YT + "/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF"      # Classical ML weeks only
SQ_STATS = YT + "/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9"
SQ_TREES = YT + "/playlist?list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe"
SQ_NN = YT + "/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1"
KARPATHY_Z2H = YT + "/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ"
CS229_LECTURES = YT + "/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU"
SENTDEX_NNFS = YT + "/playlist?list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3"

MML = "https://mml-book.github.io"
ISL = "https://www.statlearning.com"
D2L = "https://d2l.ai"
NIELSEN = "http://neuralnetworksanddeeplearning.com"
FRIEDMAN = "https://dafriedman97.github.io/mlbook/content/introduction.html"
ML_YEARNING = "https://info.deeplearning.ai/machine-learning-yearning-book"
MLSYS = "https://mlsysbook.ai"
HUYEN_INTERVIEWS = "https://huyenchip.com/ml-interviews-book/"
HUYEN_DMLS = "https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/"
SRE_BOOK = "https://sre.google/sre-book/table-of-contents/"
TURING_WAY = "https://book.the-turing-way.org"
PY_DS_HANDBOOK = "https://jakevdp.github.io/PythonDataScienceHandbook/"

MADE_WITH_ML = "https://github.com/GokuMohandas/Made-With-ML"
MWML_COURSE = "https://madewithml.com/courses/mlops/"
FSDL = "https://fullstackdeeplearning.com/course/2022/"
FSDL_LLM = "https://fullstackdeeplearning.com/llm-bootcamp/"
CS329S = "https://web.stanford.edu/class/cs329s/"
DATACAMP_MLE = "https://www.datacamp.com/tracks/machine-learning-engineer"
MS_ML_BEGINNERS = "https://github.com/microsoft/ML-For-Beginners"
MS_AI_BEGINNERS = "https://github.com/microsoft/AI-For-Beginners"
MS_GENAI = "https://github.com/microsoft/generative-ai-for-beginners"
MS_AGENTS = "https://github.com/microsoft/ai-agents-for-beginners"
ML_FROM_SCRATCH = "https://github.com/eriklindernoren/ML-From-Scratch"
RASBT_ML_BOOK = "https://github.com/rasbt/machine-learning-book"
RASBT_LLM = "https://github.com/rasbt/LLMs-from-scratch"
HANDS_ON_LLM = "https://github.com/HandsOnLLM/Hands-On-Large-Language-Models"
PYTORCH_DL = "https://github.com/mrdbourke/pytorch-deep-learning"
LLM_HANDBOOK = "https://github.com/PacktPublishing/LLM-Engineers-Handbook"
AI_ENG_HUB = "https://github.com/patchy631/ai-engineering-hub"
PATHWAY = "https://github.com/pathwaycom/llm-app"
HF_LLM_COURSE = "https://huggingface.co/learn/llm-course/chapter1/1"
AI_ENGINEERING_BOOK = "AI Engineering — Chip Huyen (paid)"
FASTAPI_DOCS = "https://fastapi.tiangolo.com/"


WEEK_RESOURCES = {

# =========================== MACHINE LEARNING ===========================

# --- Python fluency & DS&A refresh ---
"Python Fundamentals": [
    ("video", "freeCodeCamp: Learn Python — Full Course for Beginners", YT + "/watch?v=rfscVS0vtbw"),
    ("course", "Harvard CS50P: Introduction to Programming with Python", "https://cs50.harvard.edu/python/"),
    ("book", "Think Python, 2nd ed. (free)", "https://greenteapress.com/wp/think-python-2e/"),
    ("repo", "jackfrued/Python-100-Days", "https://github.com/jackfrued/Python-100-Days"),
    ("repo", "Asabeneh/30-Days-Of-Python", "https://github.com/Asabeneh/30-Days-Of-Python"),
    ("video", "sentdex (channel — practical Python tutorials)", YT + "/@sentdex"),
],
"Data Structures & Algorithms": [
    ("course", "MIT 6.006: Introduction to Algorithms (OCW)", "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/"),
    ("book", "Problem Solving with Algorithms & Data Structures using Python (free)", "https://runestone.academy/ns/books/published/pythonds3/index.html"),
    ("video", "NeetCode (channel — algorithm walkthroughs)", YT + "/@NeetCode"),
    ("doc", "NeetCode Roadmap — what to practice, in order", "https://neetcode.io/roadmap"),
],
"Pythonic Tooling": [
    ("video", "freeCodeCamp: Git & GitHub Crash Course", YT + "/watch?v=mAFoROnOfHs"),
    ("book", "Python Data Science Handbook (free — NumPy & pandas chapters)", PY_DS_HANDBOOK),
    ("book", "Pro Git (free)", "https://git-scm.com/book/en/v2"),
    ("doc", "NumPy — official learning resources", "https://numpy.org/learn/"),
    ("doc", "pandas — 10 minutes to pandas", "https://pandas.pydata.org/docs/user_guide/10min.html"),
    ("doc", "Python venv tutorial", "https://docs.python.org/3/tutorial/venv.html"),
],

# --- Math for ML ---
"Linear Algebra": [
    ("video", "3Blue1Brown: Essence of Linear Algebra", B3B_LINALG),
    ("course", "MIT 18.06: Linear Algebra — Gilbert Strang (OCW)", "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"),
    ("book", "Mathematics for Machine Learning (free — linear algebra chapters)", MML),
],
"Calculus": [
    ("video", "3Blue1Brown: Essence of Calculus", B3B_CALC),
    ("video", "3Blue1Brown: Backpropagation calculus (the chain rule in action)", YT + "/watch?v=tIeHLnjs5U8"),
    ("video", "StatQuest: Gradient Descent, Step-by-Step", YT + "/watch?v=sDv4f4s2SB8"),
    ("book", "Mathematics for Machine Learning (free — vector calculus chapter)", MML),
],
"Probability & Statistics": [
    ("video", "3Blue1Brown: Essence of Probability (playlist)", B3B_PROB),
    ("video", "StatQuest: Statistics Fundamentals playlist", SQ_STATS),
    ("course", "Harvard Stat 110: Probability (Joe Blitzstein)", "https://projects.iq.harvard.edu/stat110"),
    ("book", "Think Stats, 2nd ed. (free)", "https://greenteapress.com/wp/think-stats-2e/"),
    ("book", "Mathematics for Machine Learning (free — probability chapter)", MML),
],

# --- Classical ML (the ONLY weeks that use the StatQuest ML playlist) ---
"Regression": [
    ("video", "StatQuest with Josh Starmer: Machine Learning playlist", SQ_ML),
    ("course", "Stanford CS229 (Andrew Ng) — lecture playlist", CS229_LECTURES),
    ("book", "An Introduction to Statistical Learning (free — linear regression & regularization)", ISL),
    ("repo", "rasbt/machine-learning-book", RASBT_ML_BOOK),
    ("repo", "microsoft/ML-For-Beginners (regression lessons)", MS_ML_BEGINNERS),
],
"Classification": [
    ("video", "StatQuest with Josh Starmer: Machine Learning playlist", SQ_ML),
    ("course", "Stanford CS229 (Andrew Ng) — lecture playlist", CS229_LECTURES),
    ("book", "An Introduction to Statistical Learning (free — classification chapter)", ISL),
    ("repo", "microsoft/ML-For-Beginners (classification lessons)", MS_ML_BEGINNERS),
    ("repo", "rasbt/machine-learning-book", RASBT_ML_BOOK),
],
"Ensemble Methods": [
    ("video", "StatQuest with Josh Starmer: Machine Learning playlist", SQ_ML),
    ("video", "StatQuest: Random Forests, Part 1", YT + "/watch?v=J4Wdy0Wc_xQ"),
    ("video", "StatQuest: Gradient Boost, Part 1", YT + "/watch?v=3CC4N4z3GJc"),
    ("video", "StatQuest: XGBoost, Part 1", YT + "/watch?v=OtD8wVaFm6E"),
    ("book", "An Introduction to Statistical Learning (free — tree-based methods)", ISL),
    ("doc", "scikit-learn: Ensemble methods", "https://scikit-learn.org/stable/modules/ensemble.html"),
    ("doc", "XGBoost documentation", "https://xgboost.readthedocs.io/"),
],
"Model Evaluation": [
    ("video", "StatQuest with Josh Starmer: Machine Learning playlist", SQ_ML),
    ("video", "StatQuest: Cross Validation", YT + "/watch?v=fSytzGwwBVw"),
    ("video", "StatQuest: ROC and AUC, Clearly Explained", YT + "/watch?v=4jRBRDbJemM"),
    ("video", "StatQuest: Bias and Variance", YT + "/watch?v=EuBBz3bI-aA"),
    ("book", "Machine Learning Yearning — Andrew Ng (free — dev/test sets, error analysis)", ML_YEARNING),
    ("book", "An Introduction to Statistical Learning (free — resampling methods)", ISL),
    ("doc", "scikit-learn: Model evaluation", "https://scikit-learn.org/stable/modules/model_evaluation.html"),
],

# --- ML from scratch ---
"Implementing Regression": [
    ("video", "StatQuest: Gradient Descent, Step-by-Step", YT + "/watch?v=sDv4f4s2SB8"),
    ("course", "Stanford CS229 (Andrew Ng) — lecture playlist (linear regression & gradient descent)", CS229_LECTURES),
    ("book", "Machine Learning from Scratch — Danny Friedman (free online book)", FRIEDMAN),
    ("repo", "eriklindernoren/ML-From-Scratch", ML_FROM_SCRATCH),
    ("video", "sentdex (channel — 'Machine Learning with Python' builds regression by hand)", YT + "/@sentdex"),
],
"Implementing Classifiers": [
    ("book", "Machine Learning from Scratch — Danny Friedman (free online book)", FRIEDMAN),
    ("repo", "eriklindernoren/ML-From-Scratch (k-NN, decision trees)", ML_FROM_SCRATCH),
    ("video", "StatQuest: Decision Trees playlist", SQ_TREES),
    ("video", "sentdex (channel — k-NN and SVM from scratch)", YT + "/@sentdex"),
    ("repo", "rasbt/machine-learning-book", RASBT_ML_BOOK),
],
"Implementing Neural Nets": [
    ("video", "Andrej Karpathy: Building micrograd (backprop from scratch)", YT + "/watch?v=VMj-3S1tku0"),
    ("video", "sentdex: Neural Networks from Scratch (playlist)", SENTDEX_NNFS),
    ("book", "Neural Networks and Deep Learning — Michael Nielsen (free)", NIELSEN),
    ("repo", "Sentdex/nnfs_book (code for 'Neural Networks from Scratch')", "https://github.com/Sentdex/nnfs_book"),
    ("repo", "eriklindernoren/ML-From-Scratch (neural network modules)", ML_FROM_SCRATCH),
    ("video", "3Blue1Brown: Neural Networks playlist (backprop intuition)", B3B_NN),
],

# --- Deep learning foundations ---
"Neural Network Basics": [
    ("video", "3Blue1Brown: Neural Networks playlist", B3B_NN),
    ("video", "StatQuest: Neural Networks / Deep Learning playlist", SQ_NN),
    ("course", "MIT 6.S191: Introduction to Deep Learning", "https://introtodeeplearning.com"),
    ("book", "Neural Networks and Deep Learning — Michael Nielsen (free)", NIELSEN),
    ("repo", "mrdbourke/pytorch-deep-learning", PYTORCH_DL),
    ("repo", "microsoft/AI-For-Beginners (neural network lessons)", MS_AI_BEGINNERS),
],
"Training Neural Nets": [
    ("video", "Andrej Karpathy: Neural Networks — Zero to Hero", KARPATHY_Z2H),
    ("video", "3Blue1Brown: Neural Networks playlist (gradient descent & backprop chapters)", B3B_NN),
    ("book", "Dive into Deep Learning (free — optimization & training chapters)", D2L),
    ("book", "Neural Networks and Deep Learning — Michael Nielsen (free — backpropagation chapter)", NIELSEN),
    ("repo", "mrdbourke/pytorch-deep-learning", PYTORCH_DL),
    ("video", "freeCodeCamp: PyTorch for Deep Learning — Daniel Bourke (full course)", YT + "/watch?v=V_xro1bcAuA"),
],
"Convolutional Networks": [
    ("course", "Stanford CS231n: CNNs for Visual Recognition", "https://cs231n.stanford.edu/"),
    ("course", "MIT 6.S191: Introduction to Deep Learning", "https://introtodeeplearning.com"),
    ("book", "Dive into Deep Learning (free — convolutional networks chapters)", D2L),
    ("repo", "mrdbourke/pytorch-deep-learning (computer vision section)", PYTORCH_DL),
    ("repo", "microsoft/AI-For-Beginners (computer vision lessons)", MS_AI_BEGINNERS),
    ("video", "freeCodeCamp: PyTorch for Deep Learning — Daniel Bourke (full course)", YT + "/watch?v=V_xro1bcAuA"),
],
"Sequence Models": [
    ("course", "Stanford CS224n: NLP with Deep Learning", "https://web.stanford.edu/class/cs224n/"),
    ("video", "StatQuest: LSTM, Clearly Explained", YT + "/watch?v=YCzL96nL7j0"),
    ("video", "StatQuest: Attention for Neural Networks, Clearly Explained", YT + "/watch?v=PSs6nxngL6k"),
    ("book", "Dive into Deep Learning (free — recurrent networks & attention)", D2L),
    ("doc", "Andrej Karpathy: The Unreasonable Effectiveness of RNNs", "http://karpathy.github.io/2015/05/21/rnn-effectiveness/"),
    ("repo", "microsoft/AI-For-Beginners (RNN & NLP lessons)", MS_AI_BEGINNERS),
],

# --- Applied / production-adjacent ML ---
"Feature Engineering": [
    ("video", "StatQuest: One-Hot, Label, Target and K-Fold Target Encoding", YT + "/watch?v=589nCGeWG1w"),
    ("video", "StatQuest: Decision Trees — Feature Selection & Missing Data", YT + "/watch?v=wpNl-JwwplA"),
    ("video", "freeCodeCamp: Scikit-Learn Machine Learning Course", YT + "/watch?v=pqNCD_5r0IU"),
    ("course", "Kaggle Learn: Feature Engineering", "https://www.kaggle.com/learn/feature-engineering"),
    ("book", "Python Data Science Handbook (free — feature engineering chapter)", PY_DS_HANDBOOK),
    ("doc", "scikit-learn: Preprocessing data", "https://scikit-learn.org/stable/modules/preprocessing.html"),
    ("repo", "GokuMohandas/Made-With-ML", MADE_WITH_ML),
],
"Model Packaging": [
    ("video", "freeCodeCamp: Python API Development with FastAPI", YT + "/watch?v=0sOvCWFmrtA"),
    ("doc", "scikit-learn: Model persistence", "https://scikit-learn.org/stable/model_persistence.html"),
    ("doc", "joblib: Persistence / model serialization", "https://joblib.readthedocs.io/en/latest/persistence.html"),
    ("doc", "FastAPI documentation", FASTAPI_DOCS),
    ("doc", "Daniel Bourke: Stanford CS329S ML deployment tutorial", "https://www.mrdbourke.com/cs329s-machine-learning-deployment-tutorial/"),
    ("repo", "mrdbourke/cs329s-ml-deployment-tutorial", "https://github.com/mrdbourke/cs329s-ml-deployment-tutorial"),
    ("repo", "GokuMohandas/Made-With-ML", MADE_WITH_ML),
],
"End-to-End Project": [
    ("course", "Made With ML: MLOps course (design → develop → deploy)", MWML_COURSE),
    ("course", "Full Stack Deep Learning 2022 (free)", FSDL),
    ("video", "Full Stack Deep Learning (YouTube channel)", YT + "/@fullstackdeeplearning"),
    ("course", "Stanford CS329S: Machine Learning Systems Design", CS329S),
    ("book", "Machine Learning Yearning — Andrew Ng (free — how to structure an ML project)", ML_YEARNING),
    ("book", "Designing Machine Learning Systems — Chip Huyen (paid; the book behind CS329S)", HUYEN_DMLS),
    ("repo", "GokuMohandas/Made-With-ML", MADE_WITH_ML),
    ("repo", "mrdbourke/cs329s-ml-deployment-tutorial", "https://github.com/mrdbourke/cs329s-ml-deployment-tutorial"),
],

# =============================== MLOPS ==================================

# --- Docker & reproducibility ---
"Docker Fundamentals": [
    ("video", "freeCodeCamp: Docker Full Course", YT + "/watch?v=rjjES5IsPdg"),
    ("doc", "Docker: Get started", "https://docs.docker.com/get-started/"),
    ("repo", "docker/getting-started", "https://github.com/docker/getting-started"),
    ("doc", "Daniel Bourke: deploy an ML model with Docker + FastAPI", "https://www.mrdbourke.com/cs329s-machine-learning-deployment-tutorial/"),
    ("course", "DataCamp: Machine Learning Engineer track (paid)", DATACAMP_MLE),
    ("note", "Proof of work: containerize a FastAPI model server and run it from a fresh machine", ""),
],
"Reproducible Environments": [
    ("doc", "Docker: Multi-stage builds", "https://docs.docker.com/build/building/multi-stage/"),
    ("doc", "Docker: Build best practices", "https://docs.docker.com/build/building/best-practices/"),
    ("doc", "conda documentation", "https://docs.conda.io/"),
    ("book", "The Turing Way: Guide for Reproducible Research (free)", TURING_WAY),
    ("repo", "drivendataorg/cookiecutter-data-science", "https://github.com/drivendataorg/cookiecutter-data-science"),
    ("video", "freeCodeCamp: Docker Full Course", YT + "/watch?v=rjjES5IsPdg"),
],
"Docker Compose": [
    ("doc", "Docker Compose documentation", "https://docs.docker.com/compose/"),
    ("repo", "docker/awesome-compose (ready-made multi-container examples)", "https://github.com/docker/awesome-compose"),
    ("doc", "FastAPI in containers", "https://fastapi.tiangolo.com/deployment/docker/"),
    ("video", "freeCodeCamp: Docker Full Course (Compose sections)", YT + "/watch?v=rjjES5IsPdg"),
],

# --- Experiment tracking & data versioning ---
"MLflow Basics": [
    ("doc", "MLflow documentation", "https://mlflow.org/docs/latest/"),
    ("course", "Made With ML: Experiment tracking", "https://madewithml.com/courses/mlops/experiment-tracking/"),
    ("repo", "mlflow/mlflow", "https://github.com/mlflow/mlflow"),
    ("book", "Machine Learning Systems (free — MLOps chapters)", MLSYS),
    ("note", "Proof of work: add MLflow tracking to one of your existing training scripts", ""),
],
"Data Versioning": [
    ("doc", "DVC: Get started", "https://dvc.org/doc/start"),
    ("course", "Made With ML: Data versioning", "https://madewithml.com/courses/mlops/versioning/"),
    ("repo", "iterative/dvc", "https://github.com/iterative/dvc"),
    ("video", "DVC (YouTube channel)", YT + "/@DVCorg"),
],
"Hyperparameter Tracking": [
    ("doc", "Optuna documentation", "https://optuna.readthedocs.io/"),
    ("repo", "optuna/optuna", "https://github.com/optuna/optuna"),
    ("doc", "scikit-learn: Tuning hyper-parameters", "https://scikit-learn.org/stable/modules/grid_search.html"),
    ("course", "Made With ML: MLOps course", MWML_COURSE),
],
"Reproducible Pipelines": [
    ("doc", "Hydra: configuration management", "https://hydra.cc/"),
    ("doc", "PyTorch: Reproducibility (seeds & determinism)", "https://pytorch.org/docs/stable/notes/randomness.html"),
    ("book", "The Turing Way: Guide for Reproducible Research (free)", TURING_WAY),
    ("course", "Made With ML: Orchestration & pipelines", "https://madewithml.com/courses/mlops/orchestration/"),
    ("repo", "drivendataorg/cookiecutter-data-science", "https://github.com/drivendataorg/cookiecutter-data-science"),
],

# --- CI/CD for ML ---
"CI Fundamentals": [
    ("video", "freeCodeCamp: Git & GitHub Crash Course", YT + "/watch?v=mAFoROnOfHs"),
    ("doc", "GitHub Actions documentation", "https://docs.github.com/actions"),
    ("course", "Made With ML: CI/CD", "https://madewithml.com/courses/mlops/cicd/"),
    ("doc", "pre-commit (linting & formatting hooks)", "https://pre-commit.com/"),
    ("repo", "actions/starter-workflows", "https://github.com/actions/starter-workflows"),
    ("note", "Proof of work: a GitHub Actions pipeline (lint + test + build) on one of your repos", ""),
],
"CD for ML Models": [
    ("doc", "Google Cloud: MLOps — continuous delivery & automation pipelines", "https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning"),
    ("course", "Made With ML: Orchestration (retraining triggers)", "https://madewithml.com/courses/mlops/orchestration/"),
    ("doc", "MLflow Model Registry", "https://mlflow.org/docs/latest/model-registry.html"),
    ("doc", "CML — Continuous Machine Learning", "https://cml.dev/"),
    ("book", "Machine Learning Systems (free — MLOps chapters)", MLSYS),
],
"Testing ML Code": [
    ("course", "Made With ML: Testing ML systems", "https://madewithml.com/courses/mlops/testing/"),
    ("doc", "pytest documentation", "https://docs.pytest.org/"),
    ("doc", "Great Expectations (data validation)", "https://docs.greatexpectations.io/"),
    ("paper", "The ML Test Score: a rubric for production readiness (Google)", "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/"),
    ("book", "Machine Learning Systems (free)", MLSYS),
],

# --- Monitoring & drift ---
"Monitoring Basics": [
    ("course", "Made With ML: Monitoring ML systems", "https://madewithml.com/courses/mlops/monitoring/"),
    ("doc", "Google: Rules of Machine Learning", "https://developers.google.com/machine-learning/guides/rules-of-ml"),
    ("book", "Google SRE Book (free — Monitoring Distributed Systems)", "https://sre.google/sre-book/monitoring-distributed-systems/"),
    ("doc", "Prometheus: Overview", "https://prometheus.io/docs/introduction/overview/"),
    ("doc", "Grafana documentation", "https://grafana.com/docs/grafana/latest/"),
    ("repo", "evidentlyai/evidently", "https://github.com/evidentlyai/evidently"),
],
"Data Drift": [
    ("course", "Evidently AI: ML observability course (free)", "https://www.evidentlyai.com/ml-observability-course"),
    ("doc", "Evidently AI: What is data drift?", "https://www.evidentlyai.com/ml-in-production/data-drift"),
    ("course", "Made With ML: Monitoring ML systems", "https://madewithml.com/courses/mlops/monitoring/"),
    ("doc", "SciPy: Kolmogorov-Smirnov two-sample test", "https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html"),
    ("repo", "evidentlyai/evidently", "https://github.com/evidentlyai/evidently"),
    ("note", "Proof of work: run PSI and KS tests between a training set and a shifted copy, then log the result", ""),
],
"Model Drift": [
    ("doc", "Chip Huyen: Data distribution shifts and monitoring", "https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html"),
    ("doc", "Evidently AI: What is concept drift?", "https://www.evidentlyai.com/ml-in-production/concept-drift"),
    ("course", "Made With ML: Monitoring & orchestration", "https://madewithml.com/courses/mlops/monitoring/"),
    ("course", "Evidently AI: ML observability course (free)", "https://www.evidentlyai.com/ml-observability-course"),
],
"Observability": [
    ("doc", "OpenTelemetry documentation", "https://opentelemetry.io/docs/"),
    ("doc", "OpenTelemetry: Traces", "https://opentelemetry.io/docs/concepts/signals/traces/"),
    ("book", "Google SRE Book (free — Service Level Objectives / error budgets)", "https://sre.google/sre-book/service-level-objectives/"),
    ("book", "Google SRE Book (free — Managing Incidents)", "https://sre.google/sre-book/managing-incidents/"),
    ("doc", "Google SRE Workbook: Incident response", "https://sre.google/workbook/incident-response/"),
    ("repo", "open-telemetry/opentelemetry-python", "https://github.com/open-telemetry/opentelemetry-python"),
],

# --- Serving & scaling ---
"Model Serving Basics": [
    ("video", "freeCodeCamp: Python API Development with FastAPI", YT + "/watch?v=0sOvCWFmrtA"),
    ("doc", "FastAPI documentation", FASTAPI_DOCS),
    ("course", "Made With ML: Serving", "https://madewithml.com/courses/mlops/serving/"),
    ("doc", "Chip Huyen: Real-time machine learning — challenges and solutions", "https://huyenchip.com/2022/01/02/real-time-machine-learning-challenges-and-solutions.html"),
    ("doc", "TorchServe documentation", "https://pytorch.org/serve/"),
    ("book", "Machine Learning Systems (free — deployment chapters)", MLSYS),
],
"Scalable Serving": [
    ("video", "TechWorld with Nana: Kubernetes Tutorial for Beginners", YT + "/watch?v=X48VuDVv0do"),
    ("doc", "Kubernetes Basics (interactive tutorial)", "https://kubernetes.io/docs/tutorials/kubernetes-basics/"),
    ("doc", "Kubernetes: Horizontal Pod Autoscaling", "https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/"),
    ("book", "Google SRE Book (free — Load Balancing at the Frontend)", "https://sre.google/sre-book/load-balancing-frontend/"),
    ("doc", "Redis documentation (caching)", "https://redis.io/docs/"),
    ("note", "Proof of work: load-test your FastAPI inference server and record requests/second", ""),
],
"Serving Frameworks": [
    ("doc", "TorchServe documentation", "https://pytorch.org/serve/"),
    ("doc", "TensorFlow Serving guide", "https://www.tensorflow.org/tfx/guide/serving"),
    ("doc", "ONNX Runtime documentation", "https://onnxruntime.ai/docs/"),
    ("doc", "NVIDIA Triton Inference Server documentation", "https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html"),
    ("repo", "triton-inference-server/tutorials", "https://github.com/triton-inference-server/tutorials"),
],
"Cost & Latency Optimization": [
    ("doc", "ONNX Runtime: Quantization", "https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html"),
    ("doc", "PyTorch: Quantization", "https://pytorch.org/docs/stable/quantization.html"),
    ("doc", "Triton: Dynamic batching", "https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html"),
    ("doc", "Kubernetes: Horizontal Pod Autoscaling", "https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/"),
    ("book", "Machine Learning Systems (free — efficient AI & optimization chapters)", MLSYS),
],

# ============================ AI ENGINEER ===============================

# --- LLM fundamentals ---
"Transformer Architecture": [
    ("video", "3Blue1Brown: But what is a GPT? (visual intro to transformers)", YT + "/watch?v=wjZofJX0v4M"),
    ("video", "3Blue1Brown: Attention in transformers, visually explained", YT + "/watch?v=eMlx5fFNoYc"),
    ("video", "Andrej Karpathy: Let's build GPT from scratch", YT + "/watch?v=kCc8FmEb1nY"),
    ("doc", "Jay Alammar: The Illustrated Transformer", "https://jalammar.github.io/illustrated-transformer/"),
    ("paper", "Attention Is All You Need", "https://arxiv.org/abs/1706.03762"),
    ("course", "Stanford CS25: Transformers United", "https://web.stanford.edu/class/cs25/"),
    ("repo", "rasbt/LLMs-from-scratch", RASBT_LLM),
    ("repo", "HandsOnLLM/Hands-On-Large-Language-Models", HANDS_ON_LLM),
],
"Tokenization & Embeddings": [
    ("video", "Andrej Karpathy: Let's build the GPT Tokenizer", YT + "/watch?v=zduSFxRajkE"),
    ("course", "Hugging Face LLM Course (free)", HF_LLM_COURSE),
    ("book", "Speech and Language Processing — Jurafsky & Martin (free draft)", "https://web.stanford.edu/~jurafsky/slp3/"),
    ("doc", "Jay Alammar: The Illustrated Word2vec", "https://jalammar.github.io/illustrated-word2vec/"),
    ("repo", "rasbt/LLMs-from-scratch (data & tokenization chapter)", RASBT_LLM),
    ("repo", "HandsOnLLM/Hands-On-Large-Language-Models", HANDS_ON_LLM),
],
"Pretraining & Fine-tuning": [
    ("video", "Andrej Karpathy: Deep Dive into LLMs like ChatGPT", YT + "/watch?v=7xTGNNLPyMI"),
    ("course", "Hugging Face LLM Course (free — fine-tuning chapters)", HF_LLM_COURSE),
    ("paper", "LoRA: Low-Rank Adaptation of Large Language Models", "https://arxiv.org/abs/2106.09685"),
    ("paper", "QLoRA: Efficient Finetuning of Quantized LLMs", "https://arxiv.org/abs/2305.14314"),
    ("repo", "rasbt/LLMs-from-scratch (pretraining & fine-tuning)", RASBT_LLM),
    ("repo", "PacktPublishing/LLM-Engineers-Handbook (free companion repo)", LLM_HANDBOOK),
],
"LLM Evaluation": [
    ("video", "Andrej Karpathy: Intro to Large Language Models", YT + "/watch?v=zjkBMFhNj_g"),
    ("course", "DeepLearning.AI: Automated Testing for LLMOps", "https://www.deeplearning.ai/courses/automated-testing-llmops"),
    ("doc", "Hugging Face: Perplexity of fixed-length models", "https://huggingface.co/docs/transformers/perplexity"),
    ("doc", "Stanford HELM: Holistic Evaluation of Language Models", "https://crfm.stanford.edu/helm/"),
    ("repo", "EleutherAI/lm-evaluation-harness", "https://github.com/EleutherAI/lm-evaluation-harness"),
    ("book", AI_ENGINEERING_BOOK + " — evaluation chapters", ""),
],

# --- Prompting, RAG, agents ---
"Prompt Engineering": [
    ("course", "DeepLearning.AI: ChatGPT Prompt Engineering for Developers", "https://www.deeplearning.ai/courses/chatgpt-prompt-eng"),
    ("doc", "OpenAI: Prompt engineering guide", "https://platform.openai.com/docs/guides/prompt-engineering"),
    ("doc", "Anthropic: Prompt engineering overview", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"),
    ("doc", "Prompt Engineering Guide (DAIR.AI)", "https://www.promptingguide.ai/"),
    ("paper", "Chain-of-Thought Prompting Elicits Reasoning in LLMs", "https://arxiv.org/abs/2201.11903"),
    ("repo", "microsoft/generative-ai-for-beginners (prompt engineering lessons)", MS_GENAI),
    ("course", "Full Stack LLM Bootcamp (free)", FSDL_LLM),
],
"Embeddings & Vector Search": [
    ("course", "DeepLearning.AI: Vector Databases — From Embeddings to Applications", "https://www.deeplearning.ai/courses/vector-databases-embeddings-applications"),
    ("course", "DeepLearning.AI: Embedding Models — Architecture to Implementation", "https://www.deeplearning.ai/courses/embedding-models-from-architecture-to-implementation/"),
    ("doc", "Pinecone Learn", "https://www.pinecone.io/learn/"),
    ("doc", "Weaviate Academy", "https://academy.weaviate.io/"),
    ("doc", "Sentence Transformers (Hugging Face)", "https://huggingface.co/sentence-transformers"),
    ("repo", "facebookresearch/faiss", "https://github.com/facebookresearch/faiss"),
    ("book", "Speech and Language Processing (free — vector semantics chapter)", "https://web.stanford.edu/~jurafsky/slp3/"),
],
"RAG Fundamentals": [
    ("video", "freeCodeCamp: Learn RAG From Scratch (LangChain engineer)", YT + "/watch?v=sVcwVQRHIc8"),
    ("course", "DeepLearning.AI: Retrieval Augmented Generation", "https://www.deeplearning.ai/courses/retrieval-augmented-generation"),
    ("doc", "LangChain: RAG tutorial", "https://python.langchain.com/docs/tutorials/rag/"),
    ("doc", "LlamaIndex: Query engines", "https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/"),
    ("repo", "microsoft/generative-ai-for-beginners (RAG & vector DB lessons)", MS_GENAI),
    ("repo", "patchy631/ai-engineering-hub (RAG apps)", AI_ENG_HUB),
],
"Advanced RAG": [
    ("course", "DeepLearning.AI: Building and Evaluating Advanced RAG", "https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/"),
    ("course", "DeepLearning.AI: Advanced Retrieval for AI with Chroma", "https://www.deeplearning.ai/courses/advanced-retrieval-for-ai/"),
    ("course", "DeepLearning.AI: Knowledge Graphs for RAG", "https://www.deeplearning.ai/courses/knowledge-graphs-rag"),
    ("doc", "Weaviate: Hybrid search", "https://docs.weaviate.io/weaviate/concepts/search/hybrid-search"),
    ("doc", "Cohere: Rerank", "https://docs.cohere.com/docs/reranking"),
    ("doc", "LlamaIndex: Query transformations", "https://docs.llamaindex.ai/en/stable/module_guides/querying/query_transformations/"),
    ("repo", "pathwaycom/llm-app (production RAG pipelines)", PATHWAY),
],
"Agents": [
    ("repo", "microsoft/ai-agents-for-beginners", MS_AGENTS),
    ("doc", "Anthropic: Building effective agents", "https://www.anthropic.com/engineering/building-effective-agents"),
    ("course", "DeepLearning.AI: Functions, Tools and Agents with LangChain", "https://www.deeplearning.ai/courses/functions-tools-agents-langchain"),
    ("paper", "ReAct: Synergizing Reasoning and Acting in LLMs", "https://arxiv.org/abs/2210.03629"),
    ("doc", "LangGraph documentation", "https://docs.langchain.com/oss/python/langgraph/overview"),
    ("course", "LangChain Academy", "https://academy.langchain.com/"),
    ("doc", "OpenAI: Function calling", "https://platform.openai.com/docs/guides/function-calling"),
],

# --- LLM apps in production ---
"Serving LLM Apps": [
    ("repo", "PacktPublishing/LLM-Engineers-Handbook (free companion repo)", LLM_HANDBOOK),
    ("video", "freeCodeCamp: Python API Development with FastAPI", YT + "/watch?v=0sOvCWFmrtA"),
    ("doc", "FastAPI: StreamingResponse", "https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse"),
    ("doc", "FastAPI: Concurrency and async / await", "https://fastapi.tiangolo.com/async/"),
    ("doc", "vLLM documentation", "https://docs.vllm.ai/"),
    ("doc", "Hugging Face: Text Generation Inference", "https://huggingface.co/docs/text-generation-inference/en/index"),
    ("book", "Building Generative AI Services with FastAPI (paid)", ""),
    ("repo", "patchy631/ai-engineering-hub", AI_ENG_HUB),
],
"LLM Ops": [
    ("course", "DeepLearning.AI: LLMOps", "https://www.deeplearning.ai/courses/llmops"),
    ("course", "Full Stack LLM Bootcamp (free)", FSDL_LLM),
    ("doc", "LangSmith documentation (prompt versioning & tracing)", "https://docs.smith.langchain.com/"),
    ("doc", "Weights & Biases Weave", "https://weave-docs.wandb.ai/"),
    ("doc", "LiteLLM (cost tracking)", "https://docs.litellm.ai/"),
    ("doc", "vLLM: Performance", "https://docs.vllm.ai/en/latest/performance/"),
    ("book", AI_ENGINEERING_BOOK, ""),
],
"Guardrails & Safety": [
    ("doc", "OWASP Top 10 for LLM Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
    ("doc", "Guardrails AI", "https://www.guardrailsai.com/"),
    ("doc", "NVIDIA NeMo Guardrails", "https://docs.nvidia.com/nemo/guardrails/latest/"),
    ("doc", "Pydantic (output validation)", "https://docs.pydantic.dev/latest/"),
    ("doc", "Microsoft Presidio (PII detection)", "https://microsoft.github.io/presidio/"),
    ("repo", "microsoft/generative-ai-for-beginners (responsible AI lesson)", MS_GENAI),
],
"Evaluation in Production": [
    ("course", "DeepLearning.AI: Evaluating AI Agents", "https://www.deeplearning.ai/courses/evaluating-ai-agents"),
    ("course", "DeepLearning.AI: Automated Testing for LLMOps", "https://www.deeplearning.ai/courses/automated-testing-llmops"),
    ("doc", "LangSmith: Evaluation", "https://docs.langchain.com/langsmith/evaluation"),
    ("doc", "Arize Phoenix", "https://phoenix.arize.com/"),
    ("repo", "explodinggradients/ragas", "https://github.com/explodinggradients/ragas"),
    ("book", AI_ENGINEERING_BOOK + " — evaluation chapters", ""),
],

# --- Advanced / research-grade ML ---
"Graph Neural Networks": [
    ("course", "Stanford CS224W: Machine Learning with Graphs", "https://web.stanford.edu/class/cs224w/"),
    ("video", "Stanford Online (channel — CS224W lecture recordings)", YT + "/@stanfordonline"),
    ("book", "Graph Representation Learning — William Hamilton (free)", "https://www.cs.mcgill.ca/~wlh/grl_book/"),
    ("doc", "Distill: A Gentle Introduction to Graph Neural Networks", "https://distill.pub/2021/gnn-intro/"),
    ("doc", "PyTorch Geometric documentation", "https://pytorch-geometric.readthedocs.io/"),
    ("repo", "pyg-team/pytorch_geometric", "https://github.com/pyg-team/pytorch_geometric"),
    ("paper", "GCN: Semi-Supervised Classification with GCNs", "https://arxiv.org/abs/1609.02907"),
    ("paper", "GAT: Graph Attention Networks", "https://arxiv.org/abs/1710.10903"),
],
"Physics-Informed ML": [
    ("video", "Steve Brunton (channel — physics-informed machine learning)", YT + "/@Eigensteve"),
    ("book", "Physics-Based Deep Learning (free online book)", "https://www.physicsbaseddeeplearning.org/"),
    ("doc", "DeepXDE documentation (PINNs)", "https://deepxde.readthedocs.io/en/latest/"),
    ("repo", "lululxvl/deepxde", "https://github.com/lululxvl/deepxde"),
    ("paper", "Neural Ordinary Differential Equations", "https://arxiv.org/abs/1806.07366"),
    ("repo", "rtqichen/torchdiffeq", "https://github.com/rtqichen/torchdiffeq"),
    ("paper", "Learning to Simulate Complex Physics with Graph Networks", "https://arxiv.org/abs/2002.09405"),
],
"Generative Models": [
    ("course", "Stanford CS236: Deep Generative Models", "https://deepgenerativemodels.github.io/"),
    ("course", "Hugging Face Diffusion Models Course", "https://huggingface.co/learn/diffusion-course/unit0/1"),
    ("book", "Understanding Deep Learning — Simon Prince (free)", "https://udlbook.github.io/udlbook/"),
    ("doc", "Lilian Weng: What are diffusion models?", "https://lilianweng.github.io/posts/2021-07-11-diffusion-models/"),
    ("repo", "huggingface/diffusers", "https://github.com/huggingface/diffusers"),
    ("paper", "Auto-Encoding Variational Bayes (VAE)", "https://arxiv.org/abs/1312.6114"),
    ("paper", "Generative Adversarial Networks", "https://arxiv.org/abs/1406.2661"),
],
"Federated & Efficient Learning": [
    ("course", "MIT 6.5940: TinyML and Efficient Deep Learning (Song Han)", "https://efficientml.ai/"),
    ("doc", "Flower: Federated learning framework", "https://flower.ai/docs/"),
    ("repo", "adap/flower", "https://github.com/adap/flower"),
    ("paper", "Communication-Efficient Learning of Deep Networks from Decentralized Data (FedAvg)", "https://arxiv.org/abs/1602.05629"),
    ("paper", "Distilling the Knowledge in a Neural Network (Hinton)", "https://arxiv.org/abs/1503.02531"),
    ("doc", "Hugging Face: Quantization overview", "https://huggingface.co/docs/transformers/main/en/quantization/overview"),
    ("book", "Machine Learning Systems (free — efficient AI chapters)", MLSYS),
],
"Reading Research Papers": [
    ("doc", "How to Read a Paper — S. Keshav", "https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf"),
    ("video", "Yannic Kilcher (channel — paper walkthroughs)", YT + "/@YannicKilcher"),
    ("doc", "Andrej Karpathy: A Recipe for Training Neural Networks", "http://karpathy.github.io/2019/04/25/recipe/"),
    ("doc", "Hugging Face Papers", "https://huggingface.co/papers"),
    ("doc", "arXiv", "https://arxiv.org/"),
    ("doc", "Google: Technical Writing courses", "https://developers.google.com/tech-writing"),
],

# --- Systems thinking for interviews ---
"ML System Design": [
    ("book", "Machine Learning Interviews — Chip Huyen (free online book)", HUYEN_INTERVIEWS),
    ("course", "Stanford CS329S: Machine Learning Systems Design", CS329S),
    ("course", "Full Stack Deep Learning 2022 (free)", FSDL),
    ("book", "Machine Learning Systems — Harvard (free online book)", MLSYS),
    ("doc", "Google: Rules of Machine Learning", "https://developers.google.com/machine-learning/guides/rules-of-ml"),
    ("book", "Designing Machine Learning Systems — Chip Huyen (paid)", HUYEN_DMLS),
    ("repo", "harvard-edge/cs249r_book (source of Machine Learning Systems)", "https://github.com/harvard-edge/cs249r_book"),
],
"Case Studies": [
    ("repo", "eugeneyan/applied-ml (real case studies from industry teams)", "https://github.com/eugeneyan/applied-ml"),
    ("doc", "Google: Recommendation systems course", "https://developers.google.com/machine-learning/recommendation"),
    ("course", "Stanford CS246: Mining Massive Datasets (recommenders)", "https://web.stanford.edu/class/cs246/"),
    ("course", "Stanford CS276: Information Retrieval & Web Search", "https://web.stanford.edu/class/cs276/"),
    ("book", "Machine Learning Interviews — Chip Huyen (free online book)", HUYEN_INTERVIEWS),
    ("repo", "chiphuyen/machine-learning-systems-design", "https://github.com/chiphuyen/machine-learning-systems-design"),
],
"Behavioral & Portfolio Prep": [
    ("doc", "Tech Interview Handbook: Behavioral interview guide", "https://www.techinterviewhandbook.org/behavioral-interview/"),
    ("doc", "Microsoft: Hiring tips", "https://careers.microsoft.com/v2/global/en/hiring-tips"),
    ("doc", "Amazon: Interviewing at Amazon", "https://www.amazon.jobs/content/en/how-we-hire/interviewing-at-amazon"),
    ("book", "Machine Learning Interviews — Chip Huyen (free online book)", HUYEN_INTERVIEWS),
    ("course", "Full Stack Deep Learning 2022 (project development)", FSDL),
],
"Mock Interviews": [
    ("video", "Exponent (channel — system design & behavioral mocks)", YT + "/@tryexponent"),
    ("video", "ByteByteGo (channel — system design)", YT + "/@ByteByteGo"),
    ("video", "NeetCode (channel — coding interviews)", YT + "/@NeetCode"),
    ("doc", "NeetCode 150 practice list", "https://neetcode.io/practice/practice/neetcode150"),
    ("book", "Machine Learning Interviews — Chip Huyen (free online book)", HUYEN_INTERVIEWS),
    ("doc", "Pramp — free peer mock interviews", "https://www.pramp.com/"),
],

# ======================= POLISH & INTERVIEW PREP =========================

"Resume & LinkedIn": [
    ("doc", "Tech Interview Handbook: Resume guide", "https://www.techinterviewhandbook.org/resume/"),
    ("doc", "Microsoft: Hiring tips", "https://careers.microsoft.com/v2/global/en/hiring-tips"),
    ("book", "Machine Learning Interviews — Chip Huyen (free online book)", HUYEN_INTERVIEWS),
    ("doc", "Jake's Resume template (Overleaf)", "https://www.overleaf.com/latex/templates/jakes-resume/syzfjbzwjncs"),
],
"Portfolio Site": [
    ("doc", "GitHub Pages documentation", "https://docs.github.com/en/pages"),
    ("doc", "Streamlit Community Cloud: deploy an app", "https://docs.streamlit.io/deploy/streamlit-community-cloud"),
    ("doc", "Hugging Face Spaces", "https://huggingface.co/docs/hub/spaces"),
    ("repo", "othneildrew/Best-README-Template", "https://github.com/othneildrew/Best-README-Template"),
    ("course", "Full Stack Deep Learning 2022 (project development)", FSDL),
],
"Technical Interview Prep": [
    ("book", "Machine Learning Interviews — Chip Huyen (free online book)", HUYEN_INTERVIEWS),
    ("video", "NeetCode (channel)", YT + "/@NeetCode"),
    ("doc", "NeetCode Roadmap", "https://neetcode.io/roadmap"),
    ("doc", "LeetCode", "https://leetcode.com/"),
    ("course", "Stanford CS229 — lecture playlist (ML theory review)", CS229_LECTURES),
    ("book", "Dive into Deep Learning (free — deep learning review)", D2L),
],
"System Design Prep": [
    ("book", "Machine Learning Interviews — Chip Huyen (free online book)", HUYEN_INTERVIEWS),
    ("course", "Stanford CS329S: Machine Learning Systems Design", CS329S),
    ("video", "ByteByteGo (channel)", YT + "/@ByteByteGo"),
    ("video", "Exponent (channel)", YT + "/@tryexponent"),
    ("book", "Machine Learning Systems — Harvard (free online book)", MLSYS),
    ("repo", "chiphuyen/machine-learning-systems-design", "https://github.com/chiphuyen/machine-learning-systems-design"),
],
"Final Mock Interviews & Outreach": [
    ("book", "Machine Learning Interviews — Chip Huyen (free online book)", HUYEN_INTERVIEWS),
    ("doc", "Pramp — free peer mock interviews", "https://www.pramp.com/"),
    ("doc", "interviewing.io", "https://interviewing.io/"),
    ("doc", "Tech Interview Handbook", "https://www.techinterviewhandbook.org/"),
    ("video", "Exponent (channel)", YT + "/@tryexponent"),
],
}
