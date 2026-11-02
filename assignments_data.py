"""
Daily assignments for the CHEF_P Roadmap Tracker.

Keyed by week_label (same keys as CURRICULUM in app.py and STATIC_CONTENT /
WEEK_RESOURCES). Each entry has:
  "tasks": {"Mon": "...", "Tue": "...", "Wed": "...", "Thu": "...", "Fri": "..."}
  "deliverable": one line describing what Saturday's submission should contain

Written to use resources already attached in WEEK_RESOURCES (resources_data.py)
plus a handful of well-known, verified open-source exercise repos / Kaggle
competitions for weeks that need concrete hands-on practice material:
  - rougier/numpy-100        https://github.com/rougier/numpy-100
  - ajcr/100-pandas-puzzles  https://github.com/ajcr/100-pandas-puzzles
  - Kaggle Titanic           https://www.kaggle.com/c/titanic
  - Kaggle House Prices      https://www.kaggle.com/c/house-prices-advanced-regression-techniques
"""

ASSIGNMENTS = {

# ---------------- Machine Learning ----------------

"Python Fundamentals": {
"tasks": {
"Mon": "From jackfrued/Python-100-Days Day 1-3 folders: write and run 3 scripts covering variables, data types, and if/else control flow.",
"Tue": "From Asabeneh/30-Days-Of-Python Day 4-5: write 5 functions (incl. one with *args/**kwargs) and 3 loops solving small problems (FizzBuzz, sum of a list, reverse a string).",
"Wed": "Watch 30 min of freeCodeCamp's Python course on functions & modules, then package today's functions into your own importable module.",
"Thu": "Write 5 list/dict comprehensions replacing 5 for-loops from your past code; comment each with the equivalent loop.",
"Fri": "Review: pick your 3 favorite exercises this week, clean them up, and push them to a new 'python-fundamentals' GitHub repo with a short README.",
},
"deliverable": "A link to your new GitHub repo with Mon-Thu's scripts, plus a short note on what felt hardest.",
},

"Data Structures & Algorithms": {
"tasks": {
"Mon": "Implement array/string problems: reverse a string in-place, find the first non-repeating character. Use NeetCode's roadmap to pick 2 'Arrays & Strings' problems.",
"Tue": "Implement a hash map from scratch (no dict literal) supporting get/set/delete, then solve 'two sum' using your own implementation.",
"Wed": "Implement a binary tree with insert + in-order traversal, and a simple graph with BFS. Use MIT 6.006 OCW's recitation notes if you get stuck.",
"Thu": "Write Big-O annotations (time + space) for every function you wrote Mon-Wed; fix the one that's worse than it needs to be.",
"Fri": "Solve 2 problems from NeetCode 150 (one Arrays, one Trees) under a 25-minute timer, no hints.",
},
"deliverable": "Your DS&A code files (array/hashmap/tree/graph) + the 2 timed NeetCode solutions, with your Big-O notes.",
},

"Pythonic Tooling": {
"tasks": {
"Mon": "Solve exercises 1-20 of rougier/numpy-100 (Neophyte + Novice sections) without looking at solutions first.",
"Tue": "Solve exercises 1-15 of ajcr/100-pandas-puzzles (Importing, DataFrame basics, selecting data).",
"Wed": "Follow freeCodeCamp's Git & GitHub Crash Course: create a repo, make 5 commits with meaningful messages, open and merge one pull request against your own branch.",
"Thu": "Set up a fresh venv for a new project, write a requirements.txt pinned to exact versions, and document the 3 commands to recreate the environment.",
"Fri": "Review: fix or finish any numpy-100 / pandas-puzzles exercises you skipped.",
},
"deliverable": "Your numpy-100 and pandas-puzzles solutions, plus a link to the GitHub repo showing your commit history.",
},

"Linear Algebra": {
"tasks": {
"Mon": "Watch 3Blue1Brown's 'Vectors' and 'Linear combinations' chapters, then hand-compute 3 matrix-vector multiplications and check them with NumPy.",
"Tue": "Implement matrix multiplication from scratch (nested loops, no np.dot) and verify against NumPy on 3 random matrices.",
"Wed": "Watch 3Blue1Brown's eigenvector chapter, then compute eigenvalues/eigenvectors of a 2x2 matrix by hand AND with np.linalg.eig.",
"Thu": "Implement a from-scratch 2D PCA (via SVD) on a small toy dataset (even 10 points) and plot the principal axis.",
"Fri": "Read the Linear Algebra chapter of Mathematics for Machine Learning (free); write 5 sentences connecting SVD to something you'll use later (e.g. recommender systems).",
},
"deliverable": "Your matrix-multiplication-from-scratch code, eigenvector hand-calculation (photo of your work is fine), and the PCA plot.",
},

"Calculus": {
"tasks": {
"Mon": "Watch 3Blue1Brown's Essence of Calculus ch.1-3, then hand-derive 5 simple functions (polynomials) and check with sympy.",
"Tue": "Implement numerical differentiation (finite differences) from scratch and compare it to your hand-derivatives from Monday.",
"Wed": "Watch the backpropagation calculus video; hand-derive the chain rule for a 2-layer toy function f(g(x)).",
"Thu": "Implement 1D gradient descent from scratch on f(x)=x^2, log the loss every step, and plot it converging.",
"Fri": "Break your own gradient descent on purpose: use a learning rate that diverges, then one that's too slow. Write 2 sentences on what you observed.",
},
"deliverable": "Your gradient descent code + convergence plot, and the 2 'broken' learning-rate experiments with what you observed.",
},

"Probability & Statistics": {
"tasks": {
"Mon": "Watch 2-3 videos from 3Blue1Brown's Essence of Probability playlist; simulate a coin-flip and dice-roll experiment in Python and compare empirical vs theoretical probability.",
"Tue": "Watch StatQuest's intro to probability distributions; plot a Normal, Binomial, and Poisson distribution with matplotlib and describe one real-world use for each.",
"Wed": "Implement Bayes' theorem from scratch on a classic example (e.g. disease testing with false positives); verify your answer against the formula.",
"Thu": "Run a basic hypothesis test (t-test) comparing two small synthetic samples using scipy.stats; explain the p-value in your own words.",
"Fri": "Read the Probability chapter of Mathematics for Machine Learning (free); write a short note on how probability shows up in a model you've already built.",
},
"deliverable": "Your Bayes' theorem code, the distribution plots, and the hypothesis test result with your plain-English explanation.",
},

"Regression": {
"tasks": {
"Mon": "Watch StatQuest's Linear Regression videos; fit scikit-learn's LinearRegression on a small dataset (e.g. Kaggle House Prices, a 3-feature subset) and report the coefficients.",
"Tue": "Implement Ridge (L2) and Lasso (L1) using scikit-learn on the same data; compare which features Lasso zeroes out.",
"Wed": "Fit a polynomial regression (degree 2 and degree 8) on a noisy sine curve; plot both and describe the overfitting you see at degree 8.",
"Thu": "Pull the real Kaggle House Prices dataset, do basic cleaning (handle missing values), and fit your first real submission-shaped model.",
"Fri": "Write a short error analysis: which predictions were most wrong, and your hypothesis why.",
},
"deliverable": "Your regression notebook (Ridge/Lasso/polynomial) plus your Kaggle House Prices first-pass model and error analysis.",
},

"Classification": {
"tasks": {
"Mon": "Watch StatQuest's Logistic Regression videos; fit logistic regression on the Kaggle Titanic dataset (basic features only).",
"Tue": "Implement k-NN using scikit-learn on the same data; try k=1, k=5, k=15 and compare accuracy.",
"Wed": "Watch StatQuest's Decision Tree video; fit a decision tree on Titanic and visualize it with sklearn.tree.plot_tree.",
"Thu": "Fit an SVM (linear and RBF kernel) on Titanic; compare accuracy against your tree and k-NN from earlier this week.",
"Fri": "Submit your best model to the real Kaggle Titanic competition (free, public leaderboard) and record your score.",
},
"deliverable": "Your 4 classifiers' code + accuracy comparison table, and a screenshot of your real Kaggle Titanic leaderboard submission.",
},

"Ensemble Methods": {
"tasks": {
"Mon": "Watch StatQuest's Random Forest, Part 1; fit a RandomForestClassifier on Titanic and compare to last week's single decision tree.",
"Tue": "Watch StatQuest's Gradient Boost, Part 1; fit GradientBoostingClassifier on the same data.",
"Wed": "Watch StatQuest's XGBoost, Part 1; install xgboost and fit XGBClassifier on Titanic, tuning n_estimators and max_depth by hand.",
"Thu": "Compare feature importances across Random Forest, Gradient Boosting, and XGBoost on the same dataset — are the top 3 features consistent?",
"Fri": "Re-submit to Kaggle Titanic with your best ensemble model; compare your new score to last week's single-model score.",
},
"deliverable": "Your 3 ensemble models' code, the feature-importance comparison, and your improved Kaggle score vs. last week.",
},

"Model Evaluation": {
"tasks": {
"Mon": "Watch StatQuest's Cross Validation video; implement 5-fold cross-validation on your best Titanic model from last week.",
"Tue": "Watch StatQuest's ROC and AUC video; plot an ROC curve and compute AUC for 2 of your models.",
"Wed": "Compute precision, recall, and F1 for your models by hand from the confusion matrix (not just sklearn's function) to be sure you understand them.",
"Thu": "Watch StatQuest's Bias and Variance video; deliberately build one overfit model and one underfit model on the same data to see both failure modes.",
"Fri": "Write a one-page model card for your best Titanic model: metrics, what it gets wrong, and when you wouldn't trust it.",
},
"deliverable": "Your cross-validation results, ROC/AUC plots, and the one-page model card.",
},

"Implementing Regression": {
"tasks": {
"Mon": "Read the opening chapter of Danny Friedman's Machine Learning from Scratch (free); implement linear regression's prediction function (X @ weights) with plain NumPy.",
"Tue": "Implement the mean-squared-error loss function and its gradient by hand (no autograd).",
"Wed": "Implement the full gradient descent training loop; train it on a toy dataset and confirm the loss decreases.",
"Thu": "Compare your from-scratch model's predictions to scikit-learn's LinearRegression on the same data — they should be close.",
"Fri": "Break it on purpose: remove feature scaling and watch it fail to converge; then fix it and write 2 sentences on why scaling mattered.",
},
"deliverable": "Your from-scratch linear regression implementation, the sklearn comparison, and the scaling experiment write-up.",
},

"Implementing Classifiers": {
"tasks": {
"Mon": "Using eriklindernoren/ML-From-Scratch as a reference (read, don't copy-paste), implement k-NN's distance + voting logic yourself.",
"Tue": "Test your k-NN against scikit-learn's KNeighborsClassifier on the same small dataset — confirm matching predictions.",
"Wed": "Implement a decision tree's Gini-impurity split-selection function from scratch (just the splitting logic, one level deep).",
"Thu": "Extend Wednesday's code into a full recursive decision tree with a max-depth stopping rule.",
"Fri": "Compare your from-scratch tree's predictions to scikit-learn's DecisionTreeClassifier on the same data.",
},
"deliverable": "Your from-scratch k-NN and decision tree code, with both compared against their scikit-learn equivalents.",
},

"Implementing Neural Nets": {
"tasks": {
"Mon": "Watch the first ~30 minutes of Andrej Karpathy's 'Building micrograd'; implement a single neuron (weights, bias, activation) by hand.",
"Tue": "Continue the micrograd video; implement forward pass through a tiny 2-layer network with plain Python (no PyTorch yet).",
"Wed": "Implement backpropagation by hand for your tiny network — compute each gradient manually, then verify with a numerical gradient check.",
"Thu": "Read a chapter of Michael Nielsen's Neural Networks and Deep Learning (free); train your tiny network on a toy XOR-style problem.",
"Fri": "Watch sentdex's Neural Networks from Scratch (first video); compare his style of implementation to your micrograd-based one.",
},
"deliverable": "Your from-scratch neuron + backprop code, the numerical gradient check, and your network successfully learning XOR (or similar).",
},

"Neural Network Basics": {
"tasks": {
"Mon": "Watch 3Blue1Brown's 'But what is a neural network?'; build your first PyTorch nn.Module (a single linear layer + activation) and inspect its weights.",
"Tue": "Implement ReLU, sigmoid, and tanh by hand (just the math) and plot all three on the same chart.",
"Wed": "Build a 3-layer PyTorch network and run a forward pass on random input, printing the shape after each layer.",
"Thu": "Swap ReLU for sigmoid in your 3-layer network and read about vanishing gradients; note what you'd expect to go wrong in a deeper version.",
"Fri": "Read 1-2 lessons from microsoft/AI-For-Beginners on neural network basics and compare their explanation to 3Blue1Brown's.",
},
"deliverable": "Your PyTorch network code, the activation-function plot, and your notes on the sigmoid/vanishing-gradient experiment.",
},

"Training Neural Nets": {
"tasks": {
"Mon": "Watch part of Andrej Karpathy's Zero to Hero (the backprop-from-scratch video); train your Neural Network Basics model on a small real dataset.",
"Tue": "Implement and compare 2 loss functions (MSE vs cross-entropy) on appropriate tasks (regression vs classification toy problems).",
"Wed": "Train the same model with plain SGD, then with Adam; plot both loss curves on one chart and compare convergence speed.",
"Thu": "Read a 'Training Neural Nets' chapter of Dive into Deep Learning (free); add a learning-rate schedule to your training loop.",
"Fri": "Deliberately overfit a small network to a tiny dataset (near-zero training loss) to confirm you understand what overfitting looks like in the loss curves.",
},
"deliverable": "Your SGD-vs-Adam comparison plot and the deliberate-overfitting experiment with its loss curve.",
},

"Convolutional Networks": {
"tasks": {
"Mon": "Watch a Stanford CS231n intro lecture segment on convolutions; implement a single 2D convolution operation by hand on a small matrix (no library).",
"Tue": "Build a small CNN in PyTorch (2 conv layers + pooling) and run it on MNIST or a small image subset.",
"Wed": "Train your CNN for a few epochs; plot training/validation accuracy per epoch.",
"Thu": "Visualize what one of your trained filters is detecting (plot the filter weights or an activation map).",
"Fri": "Read a computer-vision lesson from microsoft/AI-For-Beginners and compare your CNN's architecture choices to theirs.",
},
"deliverable": "Your hand-implemented convolution, your trained CNN code + accuracy plot, and the filter visualization.",
},

"Sequence Models": {
"tasks": {
"Mon": "Watch StatQuest's LSTM video; build a simple RNN in PyTorch and run it on a toy sequence (e.g. predicting the next number in a pattern).",
"Tue": "Swap your RNN for an LSTM on the same toy task; compare training stability between the two.",
"Wed": "Watch StatQuest's Attention video; implement a simplified attention score calculation (dot-product) by hand on a 3-token toy example.",
"Thu": "Read Andrej Karpathy's 'Unreasonable Effectiveness of RNNs' blog post; try character-level text generation on a small text file with your RNN.",
"Fri": "Compare your RNN's generated text quality at epoch 1 vs. epoch 20 — note what changed.",
},
"deliverable": "Your RNN/LSTM code, the hand-computed attention example, and your character-generation experiment's before/after output.",
},

"Feature Engineering": {
"tasks": {
"Mon": "Watch StatQuest's encoding video; apply one-hot and target encoding to a categorical dataset (e.g. Titanic) and compare resulting shapes.",
"Tue": "Apply StandardScaler and MinMaxScaler to a numeric dataset; show how k-NN's predictions change (or don't) with vs. without scaling.",
"Wed": "Watch StatQuest's decision-tree feature-selection video; use a tree's feature_importances_ to pick the top 5 features from a dataset.",
"Thu": "Engineer 2 new features yourself (e.g. a ratio or interaction term) on Titanic or House Prices and check if they improve a simple model's score.",
"Fri": "Work through 10 more exercises from ajcr/100-pandas-puzzles focused on grouping/aggregating.",
},
"deliverable": "Your encoding/scaling comparisons, the 2 engineered features with their before/after model score, and your pandas-puzzles progress.",
},

"Model Packaging": {
"tasks": {
"Mon": "Save a trained scikit-learn model with joblib, then load it in a fresh Python session and confirm predictions match.",
"Tue": "Follow freeCodeCamp's FastAPI course intro; build a minimal FastAPI app with one '/ping' endpoint.",
"Wed": "Add a '/predict' endpoint that loads your saved model once at startup and returns a prediction from POSTed JSON.",
"Thu": "Follow Daniel Bourke's CS329S deployment tutorial to containerize your FastAPI app locally with Docker.",
"Fri": "Test your API with 5 different inputs using curl or Postman; document the request/response format in a README.",
},
"deliverable": "Your FastAPI app code (with /predict endpoint), the Dockerfile, and your README documenting example requests.",
},

"End-to-End Project": {
"tasks": {
"Mon": "Design your pipeline on paper: data source -> cleaning -> training -> saved model -> API -> (future) monitoring. Write it as a short doc.",
"Tue": "Build the data pipeline step: a script that pulls/cleans your chosen dataset reproducibly (same output every run).",
"Wed": "Build the training step: a script that trains on the pipeline's output and saves a versioned model file.",
"Thu": "Connect your Model Packaging week's FastAPI server to load this week's model and serve real predictions.",
"Fri": "Deploy it somewhere reachable (Streamlit Community Cloud, Render, or Hugging Face Spaces) and get a public URL.",
},
"deliverable": "A link to your deployed project, plus the pipeline doc and all 3 script files (data, train, serve).",
},

# ---------------- MLOps ----------------

"Docker Fundamentals": {
"tasks": {
"Mon": "Follow freeCodeCamp's Docker course intro; run your first container (docker run hello-world) and explain in your own words what just happened.",
"Tue": "Write a Dockerfile for a simple Python script; build the image and run it, confirming output matches running the script natively.",
"Wed": "Dockerfile your Model Packaging FastAPI app from 2 weeks ago; build and run it, hitting /predict from outside the container.",
"Thu": "Add a volume mount so you can edit code on your host and see changes without rebuilding the image.",
"Fri": "Push your image to Docker Hub (or GitHub Container Registry) and pull it down fresh on a clean check to confirm it's portable.",
},
"deliverable": "Your Dockerfile, a screenshot of the running container serving /predict, and the registry link to your pushed image.",
},

"Reproducible Environments": {
"tasks": {
"Mon": "Pin every dependency in one of your existing projects' requirements.txt to exact versions (package==X.Y.Z).",
"Tue": "Read the Turing Way's reproducibility guide (free); delete your venv, recreate it from the pinned requirements, and confirm the app still runs identically.",
"Wed": "Rewrite your Docker Fundamentals Dockerfile as a multi-stage build (one stage installs, final stage copies only what's needed).",
"Thu": "Compare the image size before and after the multi-stage rewrite; note the difference.",
"Fri": "Set up drivendataorg/cookiecutter-data-science (or a similar template) for one of your in-progress capstone projects.",
},
"deliverable": "Your pinned requirements.txt, the multi-stage Dockerfile with before/after image sizes, and the cookiecutter project structure.",
},

"Docker Compose": {
"tasks": {
"Mon": "Read Docker's Compose documentation; write a docker-compose.yml with your FastAPI service plus a Postgres (or Redis) service.",
"Tue": "Bring both services up with one command; confirm your API can reach the database service by its service name (not localhost).",
"Wed": "Add a named volume so the database's data survives a container restart; test by restarting and checking data persists.",
"Thu": "Reference docker/awesome-compose for a pattern you haven't tried yet (e.g. adding an nginx reverse proxy) and add it to your stack.",
"Fri": "Document your whole local dev setup (one command to run everything) in a README for your project repo.",
},
"deliverable": "Your docker-compose.yml, a screenshot of all services running, and the dev-setup README.",
},

"MLflow Basics": {
"tasks": {
"Mon": "Install MLflow; wrap one of your existing training scripts with mlflow.start_run() and log 3 hyperparameters.",
"Tue": "Log metrics (accuracy, loss) at the end of training, and log the trained model itself as an MLflow artifact.",
"Wed": "Run the same training script 3 times with different hyperparameters; open the MLflow UI and compare the 3 runs side by side.",
"Thu": "Register your best run's model in the MLflow Model Registry and mark it 'staging'.",
"Fri": "Read Made With ML's experiment-tracking lesson and add one practice (e.g. tagging runs) you hadn't been doing.",
},
"deliverable": "A screenshot of your MLflow UI comparing 3 runs, plus the registered model in the registry.",
},

"Data Versioning": {
"tasks": {
"Mon": "Install DVC; follow its 'Get started' guide to turn one of your datasets into a DVC-tracked file.",
"Tue": "Make a change to your dataset (e.g. drop a column), commit the new DVC pointer, and confirm you can check out the old version with 'dvc checkout'.",
"Wed": "Set up a DVC remote (even a local folder or free cloud storage) and push your tracked data to it.",
"Thu": "Read Made With ML's data-versioning lesson; link a specific model run (from last week's MLflow) to the exact data version it was trained on.",
"Fri": "Write a short note: if you had to reproduce last month's result today, what commands would you run?",
},
"deliverable": "Your DVC-tracked dataset with at least 2 versions, and the short reproducibility note.",
},

"Hyperparameter Tracking": {
"tasks": {
"Mon": "Run a manual grid search (3x3 grid) over 2 hyperparameters on one of your models; log every run's result in a table.",
"Tue": "Install Optuna; set up a study that searches the same 2 hyperparameters with 20 trials.",
"Wed": "Compare Optuna's best result to your manual grid search — did it find something better, and in fewer trials?",
"Thu": "Add a 3rd hyperparameter to the Optuna search space and re-run; check how much the best score improves.",
"Fri": "Log your Optuna study's results into MLflow from 2 weeks ago, so all your runs live in one place.",
},
"deliverable": "Your grid-search table, the Optuna study code + best params found, and the MLflow-logged comparison.",
},

"Reproducible Pipelines": {
"tasks": {
"Mon": "Pull every magic number out of one training script into a single YAML config file; load it with a small config-loading function (or Hydra).",
"Tue": "Set a fixed random seed across numpy/torch/python's random in your training script; run it twice and confirm identical results.",
"Wed": "Read PyTorch's reproducibility notes; check whether any of your GPU operations are non-deterministic by default, and fix what you can.",
"Thu": "Write an experiment report template (markdown) that auto-fills from your config + MLflow run — config, metrics, and a one-line summary.",
"Fri": "Run your full pipeline end-to-end from the config file alone (no manual edits) and confirm it reproduces last week's result.",
},
"deliverable": "Your config file, the seed-reproducibility test result, and one filled-out experiment report.",
},

"CI Fundamentals": {
"tasks": {
"Mon": "Follow freeCodeCamp's Git & GitHub Crash Course sections on branches and pull requests; practice making a feature branch and PR against your own repo.",
"Tue": "Write your first GitHub Actions workflow: triggers on push, just runs 'python --version' to confirm the pipeline fires.",
"Wed": "Add a real step: install your requirements.txt and run any existing tests (or write one simple test if you have none).",
"Thu": "Add pre-commit with a linter (ruff or flake8) and a formatter (black); fix whatever it flags in one of your repos.",
"Fri": "Add the linter/formatter check as a required step in your GitHub Actions workflow, so bad formatting fails CI.",
},
"deliverable": "A link to your repo's Actions tab showing a green (passing) workflow run, plus the workflow YAML file.",
},

"CD for ML Models": {
"tasks": {
"Mon": "Read Google Cloud's MLOps continuous-delivery guide; sketch (on paper or in a doc) what your own retrain-and-deploy pipeline would look like.",
"Tue": "Write a script that retrains your model and compares its accuracy to the current MLflow 'production' model.",
"Wed": "Add a validation gate: the script only promotes the new model to 'production' in the MLflow registry if it beats the old one.",
"Thu": "Trigger Wednesday's script from a GitHub Actions workflow (manual trigger is fine) and confirm it runs end-to-end.",
"Fri": "Deliberately train a worse model and confirm your gate correctly refuses to promote it.",
},
"deliverable": "Your validation-gate script, the GitHub Actions workflow that runs it, and the 'refused a worse model' test result.",
},

"Testing ML Code": {
"tasks": {
"Mon": "Write 3 pytest unit tests for one of your data-preprocessing functions (e.g. does it handle missing values correctly?).",
"Tue": "Read Made With ML's testing lesson; write a data-validation test checking your dataset's column types and null rates match expectations.",
"Wed": "Write an integration test that runs your full pipeline on a tiny sample dataset end-to-end and checks it produces valid output.",
"Thu": "Deliberately corrupt your test data (wrong type in a column) and confirm your validation test catches it.",
"Fri": "Add all your tests to the GitHub Actions CI workflow from 2 weeks ago so every push runs them automatically.",
},
"deliverable": "Your test files (unit + data validation + integration) and a screenshot of them passing in CI.",
},

"Monitoring Basics": {
"tasks": {
"Mon": "Add structured logging (not just print()) to your FastAPI model server, logging each request's input and prediction.",
"Tue": "Add 2-3 custom metrics (requests count, average latency) and expose them at a '/metrics' endpoint.",
"Wed": "Read Google's Rules of ML (free); pick 3 rules relevant to your own project and write a sentence on each.",
"Thu": "Set up a free Grafana Cloud (or local Grafana) dashboard that charts one of your logged metrics over time.",
"Fri": "Set one alert rule (even a simple one, like 'latency > 2s') and test that it fires by artificially slowing your endpoint.",
},
"deliverable": "A screenshot of your metrics dashboard and the alert rule firing during your test.",
},

"Data Drift": {
"tasks": {
"Mon": "Take one of your training datasets and create a deliberately 'shifted' copy (e.g. scale one feature by 2x).",
"Tue": "Install evidently; run its data drift report comparing the original vs. shifted dataset.",
"Wed": "Implement a PSI calculation from scratch (not just the library) on one feature, and confirm it agrees with Evidently's flag.",
"Thu": "Run a Kolmogorov-Smirnov test (scipy.stats.ks_2samp) on the same feature; compare its conclusion to your PSI result.",
"Fri": "Write up what you'd do differently in production if this drift showed up on real incoming data.",
},
"deliverable": "Your Evidently drift report, the from-scratch PSI calculation, and the KS test result with your write-up.",
},

"Model Drift": {
"tasks": {
"Mon": "Read Chip Huyen's 'Data distribution shifts and monitoring' post; summarize the difference between data drift and concept drift in your own words.",
"Tue": "Simulate concept drift: retrain your model on data where the true label relationship has changed (e.g. flip some labels) and measure the accuracy drop.",
"Wed": "Build a simple performance-decay tracker: log your model's accuracy on a rolling window of 'new' labeled data as it arrives.",
"Thu": "Define a concrete retraining trigger rule for your own project (e.g. 'retrain if accuracy drops below X for Y consecutive checks').",
"Fri": "Read Evidently AI's concept-drift explainer and compare their recommended approach to the rule you wrote Thursday.",
},
"deliverable": "Your concept-drift simulation results, the performance-decay tracker code, and your written retraining trigger rule.",
},

"Observability": {
"tasks": {
"Mon": "Install OpenTelemetry; add basic tracing to your FastAPI app so each request gets a trace ID.",
"Tue": "Add a second 'service' call inside your API (even a fake delay function) and confirm your trace shows both steps with their individual timing.",
"Wed": "Read the Google SRE Book's chapter on Service Level Objectives (free); define one SLO for your own API (e.g. 'p95 latency under 500ms').",
"Thu": "Calculate your error budget for that SLO over a 30-day window, and write what you'd do if you were about to exhaust it.",
"Fri": "Read the SRE Book's 'Managing Incidents' chapter; write a one-page incident-response checklist for your own project.",
},
"deliverable": "Your tracing setup (screenshot of a trace), the SLO + error budget calculation, and the incident-response checklist.",
},

"Model Serving Basics": {
"tasks": {
"Mon": "Benchmark your FastAPI /predict endpoint's latency for a single request (time 20 calls, report average).",
"Tue": "Read Chip Huyen's 'Real-time machine learning' post; identify whether your project actually needs real-time serving or could use batch.",
"Wed": "Write a batch inference script that scores 1000 rows at once and saves results to a file; compare its total time vs. 1000 individual API calls.",
"Thu": "Read TorchServe's quickstart docs (even if you don't use it yet) and note 2 features it gives you that your hand-rolled FastAPI server doesn't.",
"Fri": "Document, for your own project, which pattern (real-time vs batch) you'd actually use in production and why.",
},
"deliverable": "Your latency benchmark numbers, the batch-vs-real-time comparison, and your written recommendation for your project.",
},

"Scalable Serving": {
"tasks": {
"Mon": "Follow TechWorld with Nana's Kubernetes tutorial intro; set up a local cluster (minikube or kind) and deploy a 'hello world' pod.",
"Tue": "Deploy your FastAPI Docker image to your local cluster as a Deployment with 2 replicas.",
"Wed": "Expose it with a Service and confirm requests get routed to both replicas (log the pod name in each response to check).",
"Thu": "Add a Horizontal Pod Autoscaler rule and load-test with a simple script to watch it scale up.",
"Fri": "Add a Redis cache in front of your most expensive prediction path; measure the latency improvement on repeated identical requests.",
},
"deliverable": "A screenshot of your 2+ replica deployment, the autoscaler scaling under load, and the cache latency before/after numbers.",
},

"Serving Frameworks": {
"tasks": {
"Mon": "Read TorchServe's documentation; package one of your PyTorch models as a .mar file and serve it locally.",
"Tue": "Send 10 requests to your TorchServe endpoint and compare response format/latency to your hand-rolled FastAPI server.",
"Wed": "Export one of your models to ONNX format; load and run it with ONNX Runtime, confirming predictions match the original.",
"Thu": "Read NVIDIA Triton's documentation overview; note which of your models (if any) would benefit from Triton's dynamic batching.",
"Fri": "Write a short comparison table: FastAPI vs TorchServe vs ONNX Runtime — when would you reach for each one?",
},
"deliverable": "Your TorchServe and ONNX Runtime setups (both serving real predictions) and the comparison table.",
},

"Cost & Latency Optimization": {
"tasks": {
"Mon": "Quantize one of your PyTorch models to int8 using torch.quantization; compare model size before/after.",
"Tue": "Compare prediction accuracy of the quantized vs. original model on a held-out test set — quantify the tradeoff.",
"Wed": "Implement simple request batching in your FastAPI server (collect requests for 50ms, run one batched forward pass).",
"Thu": "Benchmark throughput (requests/second) before and after batching under simulated concurrent load.",
"Fri": "Read Kubernetes' Horizontal Pod Autoscaler docs again with cost in mind; write 3 sentences on how you'd balance cost vs. latency for your own project.",
},
"deliverable": "Your quantization size/accuracy tradeoff numbers and the batching throughput before/after comparison.",
},

# ---------------- AI Engineer ----------------

"Transformer Architecture": {
"tasks": {
"Mon": "Watch 3Blue1Brown's 'But what is a GPT?'; read the Illustrated Transformer blog post alongside it.",
"Tue": "Implement scaled dot-product attention from scratch (just the Q/K/V math) on a tiny 4-token toy example with NumPy.",
"Wed": "Watch the start of Andrej Karpathy's 'Let's build GPT from scratch'; follow along typing the code yourself (don't just copy-paste).",
"Thu": "Continue Karpathy's GPT build; get a minimal single-head attention block running on toy data.",
"Fri": "Read the 'Attention Is All You Need' paper's architecture diagram and abstract; write 3 sentences connecting it to what you just built.",
},
"deliverable": "Your from-scratch attention implementation and your in-progress 'build GPT' code from following Karpathy's video.",
},

"Tokenization & Embeddings": {
"tasks": {
"Mon": "Watch Andrej Karpathy's 'Let's build the GPT Tokenizer'; implement a basic byte-pair encoding merge step by hand on a short string.",
"Tue": "Use a real tokenizer (e.g. tiktoken or a Hugging Face tokenizer) on 5 sentences; count tokens and note which words got split into pieces.",
"Wed": "Read the Illustrated Word2vec post; load pretrained word embeddings and find the 5 nearest neighbors of 3 words you choose.",
"Thu": "Compute cosine similarity by hand between 2 embedding vectors and verify it matches a library function's output.",
"Fri": "Try the classic 'king - man + woman' embedding arithmetic and report what vector you get back.",
},
"deliverable": "Your BPE hand-trace, the tokenizer word-splitting examples, and the embedding nearest-neighbor + arithmetic results.",
},

"Pretraining & Fine-tuning": {
"tasks": {
"Mon": "Watch part of Andrej Karpathy's 'Deep Dive into LLMs'; write 3 sentences on what 'pretraining objective' means in your own words.",
"Tue": "Read the LoRA paper's abstract and intro; explain in your own words why it needs far fewer trainable parameters than full fine-tuning.",
"Wed": "Fine-tune a small pretrained model (e.g. a small Hugging Face model) on a tiny custom dataset using a basic LoRA setup.",
"Thu": "Compare the fine-tuned model's outputs before and after training on 3 example prompts.",
"Fri": "Read the QLoRA paper's abstract; note what it adds on top of LoRA and why that matters for running on a single GPU.",
},
"deliverable": "Your LoRA fine-tuning code/notebook and the before/after output comparison on your 3 test prompts.",
},

"LLM Evaluation": {
"tasks": {
"Mon": "Watch Andrej Karpathy's 'Intro to Large Language Models'; write 3 sentences on why perplexity alone isn't enough to judge a model.",
"Tue": "Compute perplexity of a small model on a sample text using Hugging Face's perplexity guide.",
"Wed": "Pick 5 prompts relevant to your own use case and manually grade 2 different models' responses on a 1-5 scale with written justification.",
"Thu": "Read about Stanford HELM's evaluation approach; note 2 dimensions it evaluates beyond pure accuracy.",
"Fri": "Write a mini eval rubric (3-5 criteria) you'd use to judge an LLM feature before shipping it.",
},
"deliverable": "Your perplexity calculation, the 5-prompt manual grading with justifications, and your eval rubric.",
},

"Prompt Engineering": {
"tasks": {
"Mon": "Work through DeepLearning.AI's ChatGPT Prompt Engineering for Developers (free) intro lessons; try 3 of their examples yourself.",
"Tue": "Take one task and write 3 versions of a prompt (vague, specific, few-shot) and compare the outputs side by side.",
"Wed": "Add chain-of-thought instructions ('think step by step') to a reasoning-heavy prompt; compare accuracy with and without it.",
"Thu": "Build a reusable prompt template (with placeholders) for a task you'll need repeatedly in your own project.",
"Fri": "Read the Chain-of-Thought paper's abstract; write 2 sentences on why showing reasoning steps helps.",
},
"deliverable": "Your 3-version prompt comparison, the chain-of-thought before/after test, and your reusable prompt template.",
},

"Embeddings & Vector Search": {
"tasks": {
"Mon": "Work through DeepLearning.AI's Embedding Models course intro; embed 10 sentences with a sentence-transformers model.",
"Tue": "Compute pairwise cosine similarity across your 10 embedded sentences; confirm semantically similar ones score highest.",
"Wed": "Install FAISS; build a small index over your 10 embeddings and run a nearest-neighbor query.",
"Thu": "Read Pinecone Learn's intro to vector databases; set up a free-tier vector DB (Pinecone, Weaviate, or Chroma) with the same 10 vectors.",
"Fri": "Compare FAISS's and your chosen vector DB's results for the same query — do they return the same nearest neighbors?",
},
"deliverable": "Your embedding + similarity code, the FAISS index, and the vector-DB comparison results.",
},

"RAG Fundamentals": {
"tasks": {
"Mon": "Follow the freeCodeCamp 'Learn RAG From Scratch' video intro; collect 3-5 short text documents to use as your knowledge base.",
"Tue": "Chunk your documents (try ~200-word chunks) and embed each chunk; store them in a vector index.",
"Wed": "Write the retrieval step: given a query, embed it and pull the top-3 most similar chunks.",
"Thu": "Write the generation step: feed the retrieved chunks + query into an LLM prompt and get a grounded answer.",
"Fri": "Ask 3 questions your documents can answer and 1 your documents can't — confirm your RAG system handles the 'can't answer' case honestly.",
},
"deliverable": "Your full mini-RAG pipeline code and the 4 test Q&A pairs (3 answerable + 1 'I don't know') with their outputs.",
},

"Advanced RAG": {
"tasks": {
"Mon": "Add keyword search (simple TF-IDF or BM25) alongside your vector search from last week; combine both result sets for one query.",
"Tue": "Read Weaviate's hybrid search docs; implement a basic weighted combination of keyword + semantic scores.",
"Wed": "Add a query-rewriting step: before retrieval, have an LLM expand or clarify an ambiguous user query.",
"Thu": "Add reranking: retrieve 10 candidates, then use a cross-encoder (or an LLM call) to rerank down to the best 3.",
"Fri": "Test a question that needs info from 2 different chunks; see if your pipeline handles it, and note what breaks if it doesn't.",
},
"deliverable": "Your hybrid search code, the query-rewriting example, and the reranking before/after comparison.",
},

"Agents": {
"tasks": {
"Mon": "Read Anthropic's 'Building effective agents' guide; write 3 sentences on the simplest pattern that would fit your own project.",
"Tue": "Define 2 simple tools (functions) and wire up function calling so an LLM can decide to call them.",
"Wed": "Read the ReAct paper's abstract; implement a basic Reason -> Act -> Observe loop using your 2 tools from Tuesday.",
"Thu": "Give your agent a task that requires calling both tools in sequence to answer; confirm it chains them correctly.",
"Fri": "Read microsoft/ai-agents-for-beginners' multi-agent lesson; note one idea you'd want to add to your agent next.",
},
"deliverable": "Your 2 tools + function-calling setup, and the ReAct loop handling the multi-step task.",
},

"Serving LLM Apps": {
"tasks": {
"Mon": "Wrap one of your LLM calls (RAG or agent) in a FastAPI endpoint.",
"Tue": "Add streaming: return tokens as they're generated instead of waiting for the full response (FastAPI's StreamingResponse).",
"Wed": "Make your endpoint async so it can handle a second request while waiting on a slow LLM call; test with 2 concurrent requests.",
"Thu": "Read vLLM's documentation overview; note what it would give you over your hand-rolled server if you needed to serve many users.",
"Fri": "Load-test your endpoint with 10 concurrent requests and report how latency changes vs. a single request.",
},
"deliverable": "Your streaming + async FastAPI LLM endpoint and the concurrent load-test results.",
},

"LLM Ops": {
"tasks": {
"Mon": "Put your current best prompt (from any earlier week) into version control with a clear changelog comment.",
"Tue": "Make one deliberate change to the prompt; run both versions on the same 5 test inputs and compare outputs.",
"Wed": "Add token-usage logging to one of your LLM calls (input + output tokens, estimated cost per call).",
"Thu": "Run the same task through 2 different model sizes (if available) and compare cost vs. quality.",
"Fri": "Write a short LLMOps checklist (version prompts, track cost, track latency) for your own project going forward.",
},
"deliverable": "Your prompt version comparison, the cost-tracking log, and your LLMOps checklist.",
},

"Guardrails & Safety": {
"tasks": {
"Mon": "Read the OWASP Top 10 for LLM Applications; pick the 3 most relevant risks to your own project and write a sentence on each.",
"Tue": "Add output validation to one LLM endpoint: check the response is valid JSON (or whatever format you expect) before returning it.",
"Wed": "Add a basic content filter (even a simple keyword/profanity check, or an LLM-based moderation call) in front of your output.",
"Thu": "Try to break your own system with 3 adversarial inputs (prompt injection attempts); note what happened.",
"Fri": "Fix the weakest point you found Thursday and re-test with the same 3 inputs.",
},
"deliverable": "Your output-validation + content-filter code, the 3 adversarial test results, and your fix.",
},

"Evaluation in Production": {
"tasks": {
"Mon": "Add a simple thumbs-up/thumbs-down feedback field to one of your LLM endpoints' response.",
"Tue": "Log every request/response pair (prompt, output, feedback) to a file or database for later analysis.",
"Wed": "Design an A/B test structure: route 50% of requests to prompt version A, 50% to version B, and log which each request got.",
"Thu": "Read about LLM-as-judge evaluation; try using one LLM to grade another's output on 5 examples.",
"Fri": "Review your logged data from the week and write 3 observations about real usage patterns you didn't expect.",
},
"deliverable": "Your feedback-logging code, the A/B routing setup, and your 3 written observations from real usage data.",
},

"Graph Neural Networks": {
"tasks": {
"Mon": "Read Distill's 'A Gentle Introduction to Graph Neural Networks'; draw (by hand or in a tool) a small graph relevant to your own domain (e.g. transactions, molecules, social connections).",
"Tue": "Install PyTorch Geometric; load one of its built-in toy datasets and inspect its node/edge structure.",
"Wed": "Implement one message-passing step by hand on a tiny 4-node graph (average neighbor features) before using the library version.",
"Thu": "Train a basic GCN on the toy dataset from Tuesday and report its accuracy.",
"Fri": "Read the GAT paper's abstract; note what attention adds over plain GCN averaging.",
},
"deliverable": "Your hand-computed message-passing example and your trained GCN's accuracy on the toy dataset.",
},

"Physics-Informed ML": {
"tasks": {
"Mon": "Watch a Steve Brunton video on physics-informed machine learning; write 3 sentences on what makes PINNs different from a standard neural net.",
"Tue": "Read DeepXDE's quickstart docs; set up its example solving a simple 1D differential equation.",
"Wed": "Read the Neural ODE paper's abstract; compare its idea (continuous-depth) to a standard discrete-layer network in your own words.",
"Thu": "Try a basic torchdiffeq example (from rtqichen/torchdiffeq) and run it on their provided toy ODE.",
"Fri": "Write a short note connecting this week's material to your own N-Body Surrogate project (if applicable) or another simulation problem you know.",
},
"deliverable": "Your working DeepXDE and torchdiffeq examples plus your connecting note.",
},

"Generative Models": {
"tasks": {
"Mon": "Read the VAE paper's abstract; implement a minimal autoencoder (no variational part yet) on a small image dataset.",
"Tue": "Add the variational part (mean/log-variance + reparameterization trick) to turn it into a real VAE.",
"Wed": "Read the GAN paper's abstract; sketch (in writing) the generator/discriminator training loop before coding it.",
"Thu": "Read Lilian Weng's diffusion models post; write 3 sentences on how the forward noising process works.",
"Fri": "Run a Hugging Face Diffusers pipeline example (pretrained, no training needed) and generate one sample image.",
},
"deliverable": "Your VAE implementation (with reparameterization trick) and the Diffusers-generated sample image.",
},

"Federated & Efficient Learning": {
"tasks": {
"Mon": "Read the FedAvg paper's abstract; write 3 sentences on what gets sent to the server instead of raw data.",
"Tue": "Install Flower; run its basic 'Get Started' federated learning example with 2 simulated clients.",
"Wed": "Read the Knowledge Distillation (Hinton) paper's abstract; explain in your own words why matching soft probabilities beats matching hard labels.",
"Thu": "Train a small 'teacher' model and a smaller 'student' model with basic distillation on the same toy dataset; compare student-alone vs. student-distilled accuracy.",
"Fri": "Apply Hugging Face's quantization guide to shrink one of your earlier models; compare size and accuracy before/after.",
},
"deliverable": "Your Flower federated-learning run, the distillation accuracy comparison, and the quantization before/after numbers.",
},

"Reading Research Papers": {
"tasks": {
"Mon": "Read 'How to Read a Paper' by S. Keshav; apply its 3-pass method to one paper you've referenced earlier in this roadmap.",
"Tue": "Watch one Yannic Kilcher paper-breakdown video on a topic you're curious about; write down 3 things he explained that the paper alone didn't make obvious.",
"Wed": "Pick a paper with code on Papers With Code; try running its reference implementation on a small example.",
"Thu": "Write a 1-page summary of that paper in your own words: problem, method, result, limitation.",
"Fri": "Share (or save for your portfolio) your 1-page summary as the start of a 'papers I've read' log.",
},
"deliverable": "Your 1-page paper summary and notes from the 3-pass reading exercise.",
},

"ML System Design": {
"tasks": {
"Mon": "Read the opening chapters of Chip Huyen's Machine Learning Interviews (free); write out the framework she recommends in your own words.",
"Tue": "Pick a system (e.g. 'design Spotify's song recommender') and spend 20 minutes just gathering requirements and constraints — no solutioning yet.",
"Wed": "Sketch the full system (data -> training -> serving -> monitoring) for Tuesday's prompt.",
"Thu": "Write out 3 explicit trade-offs you made in your design and why (e.g. accuracy vs. latency, build vs. buy).",
"Fri": "Do a second system design prompt end-to-end, timed to 35 minutes, without stopping to research mid-way.",
},
"deliverable": "Your 2 full system design write-ups (requirements, sketch, trade-offs) from this week.",
},

"Case Studies": {
"tasks": {
"Mon": "Read 2-3 write-ups from eugeneyan/applied-ml on recommender systems; note the common pattern (candidate generation + ranking) across them.",
"Tue": "Design a recommender system case study yourself using that 2-stage pattern, for a product of your choice.",
"Wed": "Read Google's recommendation systems course intro; compare their approach to what you designed Tuesday.",
"Thu": "Design a search-ranking case study (pick any search product); note how it differs from the recommender design.",
"Fri": "Design a fraud-detection case study, paying special attention to the class-imbalance and latency constraints unique to it.",
},
"deliverable": "Your 3 case study write-ups (recommender, search ranking, fraud detection).",
},

"Behavioral & Portfolio Prep": {
"tasks": {
"Mon": "Read the Tech Interview Handbook's behavioral interview guide; list 5 of your own real project stories you could draw on.",
"Tue": "Write one full STAR-format answer (Situation, Task, Action, Result) for your strongest story, keeping Action as the longest part.",
"Wed": "Write 2 more STAR answers for different competencies (e.g. conflict, failure, leadership).",
"Thu": "Record yourself (audio or video) answering one of your STAR questions out loud, unscripted, then listen back.",
"Fri": "Rewrite your weakest STAR answer based on what you noticed Thursday.",
},
"deliverable": "Your 3 written STAR answers and notes from listening back to your recorded answer.",
},

"Mock Interviews": {
"tasks": {
"Mon": "Solve 1 NeetCode problem under a 25-minute timer, then review the official solution even if you solved it.",
"Tue": "Do a self-run system design mock (pick a NeetCode or ByteByteGo prompt), 35 minutes, talking out loud the whole time.",
"Wed": "Solve 1 more NeetCode problem of a different category than Monday's.",
"Thu": "Do a behavioral mock: answer 3 random 'tell me about a time...' questions out loud, unscripted.",
"Fri": "Do one full mixed mock: 1 coding problem + 1 behavioral question back to back, timed, no breaks.",
},
"deliverable": "Notes on what went wrong in each mock and what you'd do differently next time.",
},

"Resume & LinkedIn": {
"tasks": {
"Mon": "Read the Tech Interview Handbook's resume guide; rewrite your 3 weakest bullet points using the 'did X, measured by Y, resulting in Z' pattern.",
"Tue": "Rewrite the rest of your resume's experience section with the same pattern; cut anything that's a duty, not an accomplishment.",
"Wed": "Set up your resume in the Jake's Resume LaTeX template (or similar) for clean formatting.",
"Thu": "Rewrite your LinkedIn headline and About section to match the same language as your resume.",
"Fri": "Ask one person (mentor, peer, or an AI reviewer) for feedback on your resume draft and make 2 concrete edits based on it.",
},
"deliverable": "Your updated resume (PDF) and your updated LinkedIn About section text.",
},

"Portfolio Site": {
"tasks": {
"Mon": "Pick your 3-5 best projects from this roadmap so far; list them in priority order.",
"Tue": "Write a proper README for your #1 project: problem, approach, key decisions, results, what you'd improve.",
"Wed": "Write the same quality README for your #2 and #3 projects.",
"Thu": "Set up a simple portfolio site (GitHub Pages, Streamlit, or Hugging Face Spaces) linking all your projects.",
"Fri": "Deploy it and do a final pass: check every link works and every project has a live demo or clear screenshot.",
},
"deliverable": "A link to your live portfolio site with at least 3 well-documented projects.",
},

"Technical Interview Prep": {
"tasks": {
"Mon": "Solve 2 NeetCode problems from the Roadmap's 'Arrays & Hashing' section, timed.",
"Tue": "Review your Classical ML weeks: explain out loud (no notes) how logistic regression, decision trees, and random forests each work.",
"Wed": "Solve 2 more NeetCode problems from a different section (Trees or Graphs).",
"Thu": "Review your Deep Learning weeks: explain backpropagation and the role of an optimizer out loud, no notes.",
"Fri": "Solve 1 harder NeetCode problem untimed, then redo it timed to see how much faster you are the second time.",
},
"deliverable": "Your solved problems (code) and brief notes from your out-loud ML theory reviews.",
},

"System Design Prep": {
"tasks": {
"Mon": "Do one full ML system design mock (Chip Huyen's book or a ByteByteGo prompt), 35 minutes, write it out fully.",
"Tue": "Review your Monday answer against Chip Huyen's framework; note what you missed.",
"Wed": "Do a second system design mock on a different type of system than Monday's.",
"Thu": "Review Wednesday's answer the same way; look for a repeated gap across both mocks.",
"Fri": "Do a third mock specifically targeting the gap you found Thursday.",
},
"deliverable": "Your 3 system design mock write-ups and the specific gap you identified and targeted.",
},

"Final Mock Interviews & Outreach": {
"tasks": {
"Mon": "Do one full mock loop: 1 coding problem + 1 system design + 1 behavioral question, back to back, timed like a real interview day.",
"Tue": "Review the full loop honestly; write down your top 2 weak points from the whole roadmap.",
"Wed": "Identify 5 people to reach out to (alumni, people at target companies, your existing contacts); draft one personalized message template.",
"Thu": "Send 3 personalized outreach messages (not generic copy-paste) referencing something specific about each person's work.",
"Fri": "Set up or update your application tracker with every company/role you're pursuing and its current status.",
},
"deliverable": "Notes from your full mock loop, your outreach messages sent, and a link/screenshot of your application tracker.",
},

}
