"""
Static "Learn with AI" content for the CHEF_P Roadmap Tracker.
Hand-written, not model-generated at runtime — zero API cost, zero API key
needed. Keyed by the week_label values used in CURRICULUM inside app.py.
Each entry has: explain (short definition), teach (a compact lesson),
quiz (3 multiple-choice questions with answers).
"""

STATIC_CONTENT = {

# ---------------- Machine Learning phase ----------------

"Python Fundamentals": {
"explain": "The core building blocks of Python: variables, data types (strings, ints, lists, dicts), control flow (if/for/while), and functions. Everything else in ML/AI code is written on top of these basics.",
"teach": """**What it is**
Python fundamentals cover syntax, data types, control flow, and functions — the vocabulary and grammar you use to write any ML code.

**Why it matters**
Every library you'll use (NumPy, pandas, PyTorch) is just Python underneath. Shaky fundamentals show up later as bugs you can't debug because you don't know what a list comprehension or a `*args` actually does.

**How it works**
Variables hold data; control flow (`if`, `for`, `while`) decides what runs; functions package reusable logic. A list comprehension like `[x**2 for x in range(10)]` is just a compact `for` loop.

**Common mistake**
Mutating a list while looping over it, or using `==` when you meant `is` for identity checks — both cause silent, confusing bugs.""",
"quiz": """**Q1. What does `[x for x in range(5) if x % 2 == 0]` produce?**  
A) [0,1,2,3,4]  B) [0,2,4]  C) [1,3]  D) Error  
**Answer: B** — it's a list comprehension filtering even numbers.

**Q2. What's the difference between a list and a tuple?**  
A) No difference  B) Tuples are mutable, lists aren't  C) Lists are mutable, tuples aren't  D) Tuples can't hold numbers  
**Answer: C** — lists can be changed after creation; tuples can't.

**Q3. What does a function without a `return` statement return?**  
A) 0  B) An error  C) `None`  D) An empty string  
**Answer: C** — Python functions implicitly return `None` if nothing is specified."""
},

"Data Structures & Algorithms": {
"explain": "The standard toolkit for organizing data (arrays, hash maps, trees, graphs) and reasoning about how fast your code runs (Big-O complexity). Interview-critical and genuinely useful for writing efficient ML pipelines.",
"teach": """**What it is**
Data structures are ways to organize data (arrays, hash maps/dicts, trees, graphs); algorithms are the procedures that operate on them. Big-O notation describes how runtime/memory grows as input size grows.

**Why it matters**
ML engineering interviews test this heavily, and real pipelines slow to a crawl when you pick the wrong structure — e.g., searching a list (O(n)) instead of a set/dict (O(1)).

**How it works**
A hash map trades memory for near-instant lookups. Trees represent hierarchy (like decision trees!). Graphs represent relationships (like the GNN work later in this roadmap). Big-O counts the worst-case operations as input size `n` grows.

**Common mistake**
Assuming a Python list's `in` check is fast — it's O(n). A `set` or `dict` key lookup is O(1) on average.""",
"quiz": """**Q1. What's the average time complexity of a dictionary lookup?**  
A) O(n)  B) O(log n)  C) O(1)  D) O(n²)  
**Answer: C** — hash maps give near-constant-time lookups on average.

**Q2. Which structure is best for representing "friends of friends" relationships?**  
A) Array  B) Graph  C) Stack  D) Queue  
**Answer: B** — graphs naturally represent networked relationships.

**Q3. What does O(n²) typically indicate?**  
A) A single pass over the data  B) Nested loops over the same input  C) Constant time  D) Logarithmic search  
**Answer: B** — like comparing every pair of elements to each other."""
},

"Pythonic Tooling": {
"explain": "The everyday tools around Python itself: NumPy and pandas for data handling, virtual environments for isolating dependencies, and Git for tracking changes to your code.",
"teach": """**What it is**
The practical toolbelt: NumPy for fast numerical arrays, pandas for tabular data, virtual environments (venv/conda) to isolate project dependencies, and Git for version control.

**Why it matters**
Without this, every project pollutes the same global Python installation, dependency versions clash between projects, and you have no way to undo a mistake or collaborate safely.

**How it works**
NumPy arrays are stored in contiguous memory, so vectorized operations run in optimized C rather than slow Python loops. pandas builds on NumPy for labeled, tabular data. `python -m venv env` creates an isolated dependency sandbox per project. Git tracks every change as a commit you can inspect or revert.

**Common mistake**
Installing packages globally instead of per-project — this is exactly what causes "works on my machine" bugs later.""",
"quiz": """**Q1. Why are NumPy operations faster than plain Python loops?**  
A) NumPy uses more RAM  B) NumPy runs vectorized operations in C under the hood  C) NumPy skips validation  D) They aren't actually faster  
**Answer: B**

**Q2. What is a virtual environment for?**  
A) Running Python faster  B) Isolating a project's dependencies from others  C) Encrypting your code  D) Connecting to the cloud  
**Answer: B**

**Q3. What does `git commit` do?**  
A) Deletes old code  B) Uploads code to GitHub  C) Saves a snapshot of your changes locally  D) Installs a package  
**Answer: C** — pushing to GitHub is a separate step (`git push`)."""
},

"Linear Algebra": {
"explain": "The math of vectors and matrices — how data is represented and transformed inside every ML model, from a simple linear regression to a transformer's attention layer.",
"teach": """**What it is**
Linear algebra deals with vectors (lists of numbers) and matrices (grids of numbers) and the operations between them: addition, multiplication, transposition, and decomposition (like SVD and eigenvalues).

**Why it matters**
A neural network's weights are matrices. Training is matrix multiplication at scale. Understanding this demystifies what's actually happening when you call `model.forward()`.

**How it works**
Matrix multiplication combines rows of one matrix with columns of another to produce a new matrix — this is literally how a neural network layer transforms input data. Eigenvalues/eigenvectors describe a matrix's "natural directions" of stretching, used in PCA and elsewhere. SVD decomposes any matrix into three simpler ones, used in dimensionality reduction and recommender systems.

**Common mistake**
Confusing element-wise multiplication with matrix multiplication — they're different operations with different shape rules.""",
"quiz": """**Q1. What shape results from multiplying a (3,4) matrix by a (4,2) matrix?**  
A) (3,2)  B) (4,4)  C) (3,4)  D) Error, incompatible  
**Answer: A** — inner dimensions (4,4) must match and cancel out.

**Q2. What do eigenvectors represent?**  
A) Random directions  B) Directions a matrix only stretches, doesn't rotate  C) The matrix's inverse  D) Row sums  
**Answer: B**

**Q3. What is SVD commonly used for in ML?**  
A) Sorting data  B) Dimensionality reduction  C) String formatting  D) Loop optimization  
**Answer: B**"""
},

"Calculus": {
"explain": "The math of change — derivatives and gradients — which is how every neural network actually learns: by computing how much each weight should change to reduce error.",
"teach": """**What it is**
Calculus here means derivatives (rate of change), the chain rule (derivatives of composed functions), and gradients (derivatives with respect to multiple variables at once).

**Why it matters**
Backpropagation — how every neural network trains — is just the chain rule applied millions of times to compute how each weight affects the final loss.

**How it works**
A derivative tells you the slope of a function at a point — in ML, "how much does the loss change if I nudge this weight?" The chain rule lets you compute that through many stacked layers, one step at a time. Gradient descent then nudges each weight slightly opposite to its gradient, repeatedly, until the loss stops improving.

**Common mistake**
Thinking gradient descent finds the perfect minimum — it usually just finds a good-enough local minimum, which is fine in practice for most ML problems.""",
"quiz": """**Q1. What does a gradient represent?**  
A) A random number  B) The direction and rate of steepest increase of a function  C) The final answer  D) A type of neural network  
**Answer: B**

**Q2. Why does gradient descent move opposite to the gradient?**  
A) It doesn't  B) To increase the loss  C) To decrease the loss (move downhill)  D) To speed up training  
**Answer: C**

**Q3. What does the chain rule let you compute?**  
A) The sum of two functions  B) The derivative of a composed (nested) function  C) A matrix inverse  D) A probability  
**Answer: B** — exactly what backpropagation needs through stacked layers."""
},

"Probability & Statistics": {
"explain": "The math of uncertainty: probability distributions, Bayes' theorem, and hypothesis testing — the foundation for everything from model evaluation to A/B testing in production.",
"teach": """**What it is**
Probability quantifies uncertainty (distributions, expected values); statistics draws conclusions from data (hypothesis testing, confidence intervals); Bayes' theorem updates beliefs given new evidence.

**Why it matters**
Model outputs are often probabilities. Deciding if a new model is "really" better than the old one, or if a metric change is real vs. noise, requires statistical thinking, not just eyeballing numbers.

**How it works**
A distribution (like Normal or Bernoulli) describes how likely different outcomes are. Bayes' theorem — P(A|B) = P(B|A)P(A)/P(B) — lets you update a prior belief after seeing evidence, which underlies naive Bayes classifiers and much of modern ML reasoning. Hypothesis testing checks whether an observed effect is likely real or just random chance.

**Common mistake**
Treating a small sample's results as statistically meaningful without checking significance — a classic source of false "wins" in A/B tests.""",
"quiz": """**Q1. What does Bayes' theorem let you do?**  
A) Calculate matrix inverses  B) Update a probability given new evidence  C) Sort a list  D) Train a neural network directly  
**Answer: B**

**Q2. What is a p-value informally used for?**  
A) Measuring model accuracy  B) Estimating how likely an observed effect is due to random chance  C) Counting parameters  D) Measuring training speed  
**Answer: B**

**Q3. Which describes a probability distribution?**  
A) A single fixed number  B) A description of how likely each possible outcome is  C) A type of loop  D) A sorting algorithm  
**Answer: B**"""
},

"Regression": {
"explain": "Predicting a continuous number (like a price or a temperature) from input features, using techniques like linear regression, regularization, and polynomial fits.",
"teach": """**What it is**
Regression predicts continuous numeric outputs. Linear regression fits a straight line (or hyperplane); regularization (L1/L2) penalizes overly complex models; polynomial regression fits curves.

**Why it matters**
It's the simplest, most interpretable ML model — and often a strong baseline you should try before reaching for anything fancier.

**How it works**
Linear regression finds weights that minimize the squared difference between predictions and actual values. L2 regularization (Ridge) shrinks weights to prevent overfitting; L1 (Lasso) can shrink some weights to exactly zero, effectively selecting features. Polynomial regression adds powers of features (x², x³) to fit curved relationships, but easily overfits if taken too far.

**Common mistake**
Adding regularization without scaling your features first — regularization penalizes large weights, so unscaled features get penalized unfairly.""",
"quiz": """**Q1. What does L1 regularization uniquely enable that L2 doesn't?**  
A) Faster training  B) Driving some weights to exactly zero (feature selection)  C) Negative predictions  D) Removing the need for data  
**Answer: B**

**Q2. What problem does regularization primarily address?**  
A) Underfitting  B) Overfitting  C) Slow training  D) Missing data  
**Answer: B**

**Q3. Why can high-degree polynomial regression be risky?**  
A) It's too slow  B) It can overfit, fitting noise instead of the true pattern  C) It only works on images  D) It can't handle numbers  
**Answer: B**"""
},

"Classification": {
"explain": "Predicting a category (like spam/not-spam) rather than a number, using models like logistic regression, k-NN, decision trees, and SVMs.",
"teach": """**What it is**
Classification assigns inputs to discrete categories. Logistic regression outputs a probability; k-NN classifies by nearest neighbors; decision trees split data by feature thresholds; SVMs find the best separating boundary.

**Why it matters**
Most real-world ML problems (fraud detection, spam filtering, medical diagnosis) are classification problems, not regression.

**How it works**
Logistic regression applies a sigmoid function to a linear combination of inputs, squashing output into a 0-1 probability. k-NN looks at the `k` closest labeled examples and votes. Decision trees repeatedly split data on the feature/threshold that best separates classes. SVMs find the boundary that maximizes the margin between classes.

**Common mistake**
Using accuracy as your only metric on an imbalanced dataset (e.g., 99% non-fraud) — a model that predicts "not fraud" every time gets 99% accuracy while being useless.""",
"quiz": """**Q1. What does logistic regression output?**  
A) A category label directly  B) A probability between 0 and 1  C) A cluster ID  D) A distance  
**Answer: B**

**Q2. How does k-NN classify a new point?**  
A) By training a neural network  B) By majority vote among its k nearest labeled neighbors  C) By computing a p-value  D) By fitting a line  
**Answer: B**

**Q3. What do SVMs try to maximize?**  
A) Training speed  B) The margin between classes  C) The number of features  D) Dataset size  
**Answer: B**"""
},

"Ensemble Methods": {
"explain": "Combining many weaker models into one stronger one — Random Forests average many decision trees; Gradient Boosting and XGBoost build trees sequentially, each correcting the last one's mistakes.",
"teach": """**What it is**
Ensembles combine multiple models to get better performance than any single one. Random Forests average many independent decision trees (bagging). Gradient Boosting/XGBoost build trees sequentially, each fixing the previous tree's errors.

**Why it matters**
Ensembles consistently win on tabular data competitions and production systems — they're often the best non-deep-learning option available.

**How it works**
Random Forests train each tree on a random subset of data/features, then average predictions — reducing variance. Boosting trains trees one at a time, where each new tree specifically targets the residual errors of the combined ensemble so far, reducing bias.

**Common mistake**
Overtuning boosting hyperparameters (learning rate, number of trees) without early stopping — boosted models overfit if you keep adding trees indefinitely.""",
"quiz": """**Q1. What's the key difference between Random Forests and Gradient Boosting?**  
A) No difference  B) Forests train trees independently in parallel; boosting trains them sequentially, correcting errors  C) Forests only work on images  D) Boosting doesn't use trees  
**Answer: B**

**Q2. Why does averaging many trees (bagging) help?**  
A) It speeds up inference  B) It reduces variance/overfitting from any single tree  C) It removes the need for data  D) It guarantees 100% accuracy  
**Answer: B**

**Q3. What does XGBoost primarily optimize for versus plain gradient boosting?**  
A) Simplicity  B) Speed and regularization improvements  C) Only classification, never regression  D) Removing all randomness  
**Answer: B**"""
},

"Model Evaluation": {
"explain": "How you actually know if a model is good: cross-validation for reliable estimates, precision/recall/F1 for classification quality, ROC-AUC for ranking ability, and the bias-variance tradeoff for diagnosing problems.",
"teach": """**What it is**
A toolkit for honestly measuring model quality: cross-validation (testing on multiple data splits), precision/recall/F1 (classification quality beyond accuracy), ROC-AUC (ranking quality), and the bias-variance tradeoff (a framework for diagnosing under/overfitting).

**Why it matters**
A model that looks great on training data can be useless in production. These tools catch that before it becomes an expensive mistake.

**How it works**
Cross-validation splits data into k folds, training on k-1 and testing on the last, rotating through all folds — giving a more reliable performance estimate than a single train/test split. Precision asks "of what I flagged positive, how much was right?"; recall asks "of all actual positives, how much did I catch?" High bias means underfitting (too simple); high variance means overfitting (too sensitive to training data).

**Common mistake**
Optimizing only for accuracy on imbalanced datasets, when precision/recall/F1 tell a much more honest story.""",
"quiz": """**Q1. What does k-fold cross-validation help avoid?**  
A) Slow training  B) An unreliable estimate from a single lucky/unlucky train-test split  C) Overfitting entirely  D) The need for a test set  
**Answer: B**

**Q2. High recall with low precision means what?**  
A) The model rarely predicts positive  B) The model catches most positives but also flags many false positives  C) The model is perfect  D) The model never makes mistakes  
**Answer: B**

**Q3. High variance in a model typically indicates:**  
A) Underfitting  B) Overfitting  C) Perfect generalization  D) Too little data variety needed  
**Answer: B**"""
},

"Implementing Regression": {
"explain": "Building linear regression and gradient descent from scratch, with no libraries — the best way to actually understand what `.fit()` is doing under the hood.",
"teach": """**What it is**
Writing linear regression's prediction formula and gradient descent's weight-update loop yourself, in plain NumPy, instead of calling scikit-learn's `.fit()`.

**Why it matters**
Implementing it yourself is the fastest way to truly internalize the material from the Math for ML weeks — it turns abstract formulas into code you can trace line by line.

**How it works**
You initialize weights randomly, compute predictions (`X @ weights`), compute the loss (mean squared error), compute the gradient of that loss with respect to each weight, then update weights by subtracting a small step in the gradient's direction — repeating until the loss stabilizes.

**Common mistake**
Picking a learning rate that's too large (the loss diverges/explodes) or too small (training takes forever) — this is usually the first thing to debug when a from-scratch implementation doesn't converge.""",
"quiz": """**Q1. What happens if your learning rate is too high?**  
A) Training is just slower  B) The loss can oscillate or diverge instead of converging  C) Nothing changes  D) It guarantees a better model  
**Answer: B**

**Q2. What is the gradient telling you in this implementation?**  
A) The final answer  B) How to adjust each weight to reduce the loss  C) The dataset size  D) A random number  
**Answer: B**

**Q3. Why implement this from scratch instead of just using scikit-learn?**  
A) It's faster in production  B) To build real understanding of what the library is doing internally  C) It's required for deployment  D) scikit-learn doesn't support regression  
**Answer: B**"""
},

"Implementing Classifiers": {
"explain": "Building k-NN and a decision tree from scratch — implementing the actual distance calculations and splitting logic instead of importing them.",
"teach": """**What it is**
Coding k-NN's distance-and-vote logic and a decision tree's recursive splitting logic yourself, without scikit-learn.

**Why it matters**
It reveals exactly why decision trees can overfit (they'll keep splitting until pure, unless you stop them) and why k-NN gets slow with large datasets (it compares to every point at prediction time).

**How it works**
k-NN computes the distance from a new point to every training point, sorts by distance, takes the `k` closest, and returns the majority class. A decision tree recursively picks the feature/threshold split that best separates classes (using a metric like Gini impurity or entropy), stopping at a max depth or when nodes become pure.

**Common mistake**
Letting a from-scratch decision tree grow without a depth limit — it will perfectly memorize the training data and generalize terribly.""",
"quiz": """**Q1. What does k-NN do at prediction time?**  
A) Nothing, it precomputes everything during training  B) Computes distance to all training points and votes among the closest k  C) Trains a new model  D) Runs gradient descent  
**Answer: B**

**Q2. What metric might a decision tree use to choose a split?**  
A) Learning rate  B) Gini impurity or entropy  C) L2 norm of weights  D) p-value  
**Answer: B**

**Q3. What happens to a decision tree with no depth limit?**  
A) It underfits  B) It tends to overfit, memorizing training data  C) It becomes a linear model  D) It stops improving immediately  
**Answer: B**"""
},

"Implementing Neural Nets": {
"explain": "Coding a single perceptron and manually working through backpropagation by hand — the clearest way to demystify what's happening inside every deep learning framework.",
"teach": """**What it is**
Building a single-layer perceptron and manually deriving/coding backpropagation's weight updates, rather than letting PyTorch's autograd handle it invisibly.

**Why it matters**
Once you've done backprop by hand once, autograd stops feeling like magic — you know exactly what `.backward()` is computing.

**How it works**
A perceptron computes a weighted sum of inputs, applies an activation function, and produces an output. Backpropagation computes the gradient of the loss with respect to each weight by applying the chain rule backward through the network, layer by layer, then updates each weight via gradient descent.

**Common mistake**
Forgetting to apply the activation function's own derivative during backprop — the chain rule requires multiplying by it at every layer, not just the linear part.""",
"quiz": """**Q1. What does a perceptron compute before applying its activation function?**  
A) A random number  B) A weighted sum of its inputs  C) The final loss  D) A probability distribution  
**Answer: B**

**Q2. What does backpropagation use to compute gradients through multiple layers?**  
A) Random search  B) The chain rule  C) Bayes' theorem  D) Cross-validation  
**Answer: B**

**Q3. What is autograd (in PyTorch/TensorFlow) actually automating?**  
A) Data loading  B) The backpropagation/gradient computation you'd otherwise do by hand  C) Model deployment  D) Hyperparameter tuning  
**Answer: B**"""
},

"Neural Network Basics": {
"explain": "The building blocks of neural networks: perceptrons stacked into layers, activation functions that add non-linearity, and forward propagation — how input becomes output.",
"teach": """**What it is**
A neural network is layers of perceptron-like units. Activation functions (ReLU, sigmoid, tanh) introduce non-linearity between layers. Forward propagation is the process of pushing an input through all layers to get a prediction.

**Why it matters**
Without activation functions, stacking layers would be mathematically equivalent to a single linear layer — non-linearity is what lets networks learn complex patterns.

**How it works**
Each layer computes `activation(weights @ input + bias)`, and feeds its output as the next layer's input. ReLU (`max(0, x)`) is the most common activation today because it's simple and trains well; sigmoid squashes to 0-1, useful for output probabilities.

**Common mistake**
Using sigmoid activations throughout a deep network — it causes vanishing gradients, where early layers barely learn because gradients shrink to near-zero as they propagate backward.""",
"quiz": """**Q1. Why do neural networks need non-linear activation functions?**  
A) To slow down training  B) Without them, stacked layers collapse into one linear function  C) To save memory  D) They don't need them  
**Answer: B**

**Q2. What does ReLU compute?**  
A) 1/(1+e^-x)  B) max(0, x)  C) x²  D) log(x)  
**Answer: B**

**Q3. What problem is associated with sigmoid activations in deep networks?**  
A) Overfitting only  B) Vanishing gradients  C) Too much memory usage  D) They can't output probabilities  
**Answer: B**"""
},

"Training Neural Nets": {
"explain": "How networks actually learn: backpropagation computes gradients, loss functions measure error, and optimizers like SGD and Adam use those gradients to update weights.",
"teach": """**What it is**
Training combines a loss function (measuring how wrong predictions are), backpropagation (computing gradients of that loss), and an optimizer (using gradients to update weights) — repeated over many batches of data.

**Why it matters**
Choosing the wrong loss function or optimizer settings is one of the most common reasons a model fails to train at all.

**How it works**
Cross-entropy loss is standard for classification; MSE for regression. Backprop computes each weight's gradient. Plain SGD steps directly opposite the gradient; Adam adapts the step size per-parameter using running averages of past gradients, generally converging faster and more reliably than plain SGD.

**Common mistake**
Using MSE loss for a classification problem (or vice versa) — the loss function needs to match the task, or training signals become meaningless.""",
"quiz": """**Q1. Which loss function is standard for classification?**  
A) Mean Squared Error  B) Cross-entropy  C) L1 norm  D) Euclidean distance  
**Answer: B**

**Q2. What does Adam do differently from plain SGD?**  
A) Nothing, they're identical  B) It adapts the learning rate per parameter using gradient history  C) It doesn't use gradients  D) It only works on CPUs  
**Answer: B**

**Q3. What is backpropagation computing?**  
A) The dataset size  B) Gradients of the loss with respect to each weight  C) The learning rate  D) The number of layers needed  
**Answer: B**"""
},

"Convolutional Networks": {
"explain": "The architecture behind most image models: convolutions scan small filters across an image to detect patterns, pooling shrinks the representation, and stacked layers build up from edges to full objects.",
"teach": """**What it is**
CNNs use convolutional layers (small learnable filters slid across an image) and pooling layers (downsampling) to build image representations, from simple edges in early layers to complex objects in later ones.

**Why it matters**
CNNs dramatically reduce the number of parameters needed compared to a fully-connected network on images, by exploiting the fact that a pattern (like an edge) is useful no matter where it appears.

**How it works**
A convolutional filter is a small grid of weights that slides across the image, computing a weighted sum at each position — detecting a specific pattern anywhere it appears (translation invariance). Pooling (e.g., max-pooling) shrinks the spatial size, keeping the strongest signals and reducing computation.

**Common mistake**
Assuming CNNs only work on images — they're used for any grid-like data, including some time-series and audio applications.""",
"quiz": """**Q1. What key property makes convolutions efficient for images?**  
A) They require huge parameter counts  B) A filter detects a pattern regardless of its position (translation invariance)  C) They only work in grayscale  D) They eliminate the need for training  
**Answer: B**

**Q2. What does a pooling layer typically do?**  
A) Adds more parameters  B) Downsamples the spatial size, keeping key signals  C) Converts images to text  D) Trains the model  
**Answer: B**

**Q3. In a CNN, what do early layers typically learn to detect?**  
A) Whole objects  B) Simple patterns like edges and textures  C) Text captions  D) Nothing, they're random  
**Answer: B**"""
},

"Sequence Models": {
"explain": "Models built for ordered data like text and time series: RNNs/LSTMs process one step at a time while keeping memory of what came before, and attention lets a model directly weigh any earlier position.",
"teach": """**What it is**
Sequence models handle ordered data. RNNs process one element at a time, carrying a hidden state forward. LSTMs add gates to control what's remembered/forgotten over long sequences. Attention lets a model directly weigh the relevance of any other position in the sequence.

**Why it matters**
This is the direct predecessor to Transformers (covered later in the AI Engineer phase) — understanding why RNNs struggle with long sequences explains why attention was such a breakthrough.

**How it works**
An RNN's hidden state is updated at each timestep based on the current input and the previous hidden state, but gradients can vanish over long sequences, making it hard to learn long-range dependencies. LSTMs use gates to explicitly control information flow, mitigating this. Attention instead computes direct connections between all positions, no matter the distance.

**Common mistake**
Assuming RNNs are "outdated and useless" — they're still relevant for many smaller-scale or resource-constrained sequence tasks.""",
"quiz": """**Q1. What problem do LSTMs address compared to plain RNNs?**  
A) Slow inference  B) Difficulty learning long-range dependencies (vanishing gradients)  C) Too much memory usage  D) Inability to process text  
**Answer: B**

**Q2. What does attention allow a model to do that plain RNNs struggle with?**  
A) Process images  B) Directly relate distant positions in a sequence without stepping through every position between them  C) Reduce parameter count to zero  D) Skip training entirely  
**Answer: B**

**Q3. What is a hidden state in an RNN?**  
A) A hidden layer's weights only  B) A running summary of the sequence seen so far, updated at each step  C) The final output only  D) A type of loss function  
**Answer: B**"""
},

"Feature Engineering": {
"explain": "Transforming raw data into a form models can actually learn from: scaling numeric features, encoding categories, and selecting which features actually help.",
"teach": """**What it is**
Feature engineering turns raw data into model-ready inputs: scaling (normalizing numeric ranges), encoding (turning categories into numbers), and feature selection (removing unhelpful or redundant inputs).

**Why it matters**
Good features often matter more than model choice — a simple model with great features frequently beats a complex model with poor ones.

**How it works**
Scaling (e.g., standardization) puts features on comparable ranges, which matters a lot for distance-based models (k-NN, SVM) and gradient descent convergence. Encoding methods like one-hot encoding turn categories into binary columns. Feature selection methods (correlation checks, L1 regularization, tree-based importance) identify which inputs actually carry signal.

**Common mistake**
Fitting your scaler/encoder on the full dataset (including test data) before splitting — this leaks test information into training, inflating your evaluation results.""",
"quiz": """**Q1. Why does feature scaling matter for k-NN or gradient descent?**  
A) It doesn't matter at all  B) Features on very different scales can dominate distance calculations or destabilize training  C) It only matters for images  D) It speeds up data loading  
**Answer: B**

**Q2. What does one-hot encoding do?**  
A) Compresses data  B) Converts a categorical variable into binary indicator columns  C) Removes missing values  D) Scales numeric features  
**Answer: B**

**Q3. What's wrong with fitting a scaler on the full dataset before train/test split?**  
A) Nothing  B) It leaks test-set information into training, inflating evaluation results  C) It's required for correctness  D) It makes training slower only  
**Answer: B**"""
},

"Model Packaging": {
"explain": "Turning a trained model into something usable: saving/loading it to disk, and wrapping it in an API (like FastAPI) so other software can request predictions from it.",
"teach": """**What it is**
Model packaging covers serializing a trained model to disk (pickle, joblib, or framework-specific formats) and exposing it through an inference API so other systems can request predictions.

**Why it matters**
A model sitting in a Jupyter notebook provides zero business value — packaging is the step that actually makes it usable by a real application.

**How it works**
Saving a model captures its learned weights/parameters so you don't need to retrain every time. FastAPI lets you define an endpoint (e.g., `POST /predict`) that loads the saved model once, accepts input data, runs `.predict()`, and returns the result as JSON.

**Common mistake**
Loading the model from disk inside the request handler instead of once at startup — this makes every single request slow and wastes resources.""",
"quiz": """**Q1. Why package a model behind an API instead of leaving it in a notebook?**  
A) Notebooks are faster  B) An API lets other software actually request predictions from it  C) APIs are required by law  D) It reduces model accuracy  
**Answer: B**

**Q2. Where should you load your saved model in a FastAPI app?**  
A) Inside every request handler  B) Once, at application startup  C) Never, always retrain  D) In the frontend  
**Answer: B**

**Q3. What is the main purpose of saving (serializing) a trained model?**  
A) To make it smaller  B) To avoid retraining every time you want to use it  C) To improve accuracy  D) To visualize it  
**Answer: B**"""
},

"End-to-End Project": {
"explain": "Connecting everything so far into one working system: a data pipeline feeding a trained model, a clear split between training and serving code, and a basic live deployment.",
"teach": """**What it is**
An end-to-end project ties together data ingestion, training, and serving into one coherent pipeline — plus deploying it somewhere reachable, even simply.

**Why it matters**
This is the difference between "I know ML concepts" and "I can ship an ML system" — exactly what a portfolio project and an interview story need to demonstrate.

**How it works**
A data pipeline pulls/cleans data reproducibly. The training script produces a saved model artifact. The serving code (from Model Packaging) loads that artifact and exposes predictions. Keeping training and serving code separate (but sharing preprocessing logic) avoids training/serving skew, where the two disagree about how data should be transformed.

**Common mistake**
Duplicating preprocessing logic between training and serving code instead of sharing it — the two drifting apart is a classic silent source of production bugs.""",
"quiz": """**Q1. What is "training/serving skew"?**  
A) A model accuracy metric  B) When preprocessing differs between training and production, causing inconsistent behavior  C) A type of neural network layer  D) A data augmentation technique  
**Answer: B**

**Q2. Why should preprocessing logic be shared between training and serving?**  
A) It's not necessary  B) To prevent the two from silently disagreeing on how data is transformed  C) To make code longer  D) To slow down inference intentionally  
**Answer: B**

**Q3. What does an end-to-end ML project typically demonstrate to an interviewer?**  
A) Only theoretical knowledge  B) The ability to ship a working system, not just train a model  C) Familiarity with a single Python library  D) Nothing useful  
**Answer: B**"""
},

# ---------------- MLOps phase ----------------

"Docker Fundamentals": {
"explain": "Packaging your application and its dependencies into a portable container using images, Dockerfiles, and volumes — so it runs identically anywhere.",
"teach": """**What it is**
Docker packages code plus its dependencies into a container built from an "image," defined by a Dockerfile. Volumes let containers persist or share data with the host machine.

**Why it matters**
"Works on my machine" stops being an excuse — a Docker container runs the same way on your laptop, a teammate's machine, or a cloud server.

**How it works**
A Dockerfile lists steps to build an image (e.g., "start from Python 3.11, copy code, install requirements"). Running that image creates a container — an isolated, lightweight process with its own filesystem. Volumes mount a folder from your host machine into the container, useful for persisting data or live-editing code.

**Common mistake**
Baking secrets (API keys, passwords) directly into a Docker image — they end up permanently embedded in the image layers.""",
"quiz": """**Q1. What is the relationship between an image and a container?**  
A) They're the same thing  B) An image is a blueprint; a container is a running instance of it  C) A container builds an image  D) Neither relates to the other  
**Answer: B**

**Q2. What does a Dockerfile define?**  
A) The network configuration only  B) The steps to build a Docker image  C) A database schema  D) A Python virtual environment  
**Answer: B**

**Q3. Why is baking secrets into a Docker image risky?**  
A) It isn't risky  B) They become permanently embedded in the image's layers and can leak  C) It makes the image faster  D) Docker doesn't allow this  
**Answer: B**"""
},

"Reproducible Environments": {
"explain": "Making sure your project's dependencies are pinned and consistent — comparing conda vs venv, and using multi-stage Docker builds to keep images lean.",
"teach": """**What it is**
Reproducibility means anyone (including future-you) can recreate your exact working environment: pinned dependency versions, a clear choice between conda/venv, and multi-stage Docker builds that separate build tools from the final lean image.

**Why it matters**
"It worked last month" is a common and entirely avoidable failure mode — unpinned dependencies silently update and break things.

**How it works**
Pinning (`package==1.2.3` in requirements.txt) locks exact versions. Conda manages both Python packages and system-level dependencies (useful for scientific computing); venv is lighter and Python-only. Multi-stage Docker builds use one stage to compile/install everything, then copy only the needed artifacts into a clean final stage — keeping images small and secure.

**Common mistake**
Using `pip install package` with no version pin in a requirements file — this silently breaks reproducibility the moment a new version is released.""",
"quiz": """**Q1. Why pin exact dependency versions?**  
A) It's not necessary  B) To prevent silent breakage when a dependency updates  C) It makes installs slower  D) It's only relevant for Docker  
**Answer: B**

**Q2. What's an advantage of conda over venv?**  
A) None  B) It can manage non-Python system dependencies too  C) It's always faster  D) It doesn't need an internet connection ever  
**Answer: B**

**Q3. What's the main benefit of a multi-stage Docker build?**  
A) Slower builds  B) A smaller, cleaner final image without build-time-only tools  C) It removes the need for a Dockerfile  D) It automatically fixes bugs  
**Answer: B**"""
},

"Docker Compose": {
"explain": "Defining and running multi-container applications (like an API plus a database) with one YAML file and one command, instead of managing each container by hand.",
"teach": """**What it is**
Docker Compose lets you define multiple related containers (e.g., an API service, a database, a cache) in one `docker-compose.yml` file and start them all together with `docker compose up`.

**Why it matters**
Most real applications aren't a single container — you need a database, maybe a cache, maybe a worker process. Compose makes local development of that whole stack a one-command operation.

**How it works**
Each "service" in the YAML file maps to a container, with its image/build context, ports, environment variables, and volumes defined declaratively. Compose sets up a shared network so services can reach each other by name (e.g., your API can connect to `db:5432`).

**Common mistake**
Hardcoding `localhost` instead of the service name when connecting between containers — inside Compose's network, services reach each other by service name, not localhost.""",
"quiz": """**Q1. What problem does Docker Compose solve?**  
A) Running a single container  B) Coordinating multiple related containers with one config file  C) Replacing Python entirely  D) Writing Dockerfiles for you  
**Answer: B**

**Q2. Inside a Compose network, how does one service reach another?**  
A) Via localhost always  B) Via the other service's name as a hostname  C) They can't communicate  D) Only via the public internet  
**Answer: B**

**Q3. What command typically starts all services defined in docker-compose.yml?**  
A) docker run  B) docker compose up  C) docker build  D) docker ps  
**Answer: B**"""
},

"MLflow Basics": {
"explain": "A tool for tracking ML experiments — logging metrics, parameters, and models for every run, so you can compare experiments and manage a model registry.",
"teach": """**What it is**
MLflow tracks experiments: logging hyperparameters, metrics, and model artifacts for every training run, plus a model registry for versioning which model is "production-ready."

**Why it matters**
Without tracking, "which settings gave that good result three weeks ago?" becomes an unanswerable question — MLflow makes every run reproducible and comparable.

**How it works**
You wrap training code with `mlflow.start_run()`, then call `mlflow.log_param()` / `mlflow.log_metric()` / `mlflow.log_model()` to record everything about that run. MLflow's UI then lets you compare runs side by side. The model registry tracks versions and stages (staging, production) of a model over time.

**Common mistake**
Only logging final metrics and not the hyperparameters that produced them — making past good results impossible to reproduce.""",
"quiz": """**Q1. What does MLflow's tracking component primarily record?**  
A) Only the final model file  B) Parameters, metrics, and artifacts for each run  C) Only source code  D) Server logs  
**Answer: B**

**Q2. What is the MLflow Model Registry used for?**  
A) Storing raw data  B) Versioning and managing model lifecycle stages (e.g., staging vs production)  C) Writing Dockerfiles  D) Training models  
**Answer: B**

**Q3. Why log hyperparameters alongside metrics?**  
A) It's optional and unimportant  B) Without them, a good result can't be reproduced later  C) It slows down training  D) MLflow requires it for licensing  
**Answer: B**"""
},

"Data Versioning": {
"explain": "Tracking changes to datasets the way Git tracks changes to code, using DVC, so you can reproduce exactly which data trained which model version.",
"teach": """**What it is**
Data versioning (commonly via DVC) applies Git-like version control to datasets and pipelines — tracking which exact data snapshot produced which model.

**Why it matters**
Code being version-controlled but data not is a common gap — if your dataset changes silently, your "reproducible" pipeline isn't actually reproducible.

**How it works**
DVC stores lightweight pointer files in Git (instead of huge data files directly) while the actual data lives in remote storage (S3, GCS, etc.). Running `dvc pull` fetches the exact data version referenced by your current Git commit, keeping code and data versions locked together.

**Common mistake**
Committing large raw data files directly into Git — this bloats the repository and defeats the purpose of a lightweight version-control system.""",
"quiz": """**Q1. What problem does data versioning solve that Git alone doesn't?**  
A) Nothing, Git handles everything  B) Tracking large datasets and linking exact data versions to code/model versions  C) Writing Dockerfiles  D) Managing servers  
**Answer: B**

**Q2. How does DVC typically avoid bloating a Git repository?**  
A) It doesn't use Git at all  B) It stores lightweight pointers in Git while actual data lives in remote storage  C) It compresses all files automatically  D) It deletes old data  
**Answer: B**

**Q3. Why is it risky if your dataset changes silently without versioning?**  
A) It isn't risky  B) You lose the ability to reproduce past results or debug regressions  C) It only affects visualization  D) It makes training faster  
**Answer: B**"""
},

"Hyperparameter Tracking": {
"explain": "Systematically searching for the best model settings (grid search, random search, or smarter tools like Optuna) and comparing runs to know what actually worked.",
"teach": """**What it is**
Hyperparameter tracking covers search strategies (grid search tries all combinations; random search samples randomly; Optuna uses smarter, adaptive search) and comparing the resulting runs.

**Why it matters**
The same model architecture can perform wildly differently depending on learning rate, batch size, or regularization strength — tuning matters, but doing it blindly wastes huge amounts of compute.

**How it works**
Grid search is exhaustive but expensive as the number of hyperparameters grows. Random search often finds good combinations faster by not wasting time on unpromising regions exhaustively. Optuna goes further, using past trial results to intelligently choose the next hyperparameters to try (Bayesian-style optimization), often converging much faster than either alternative.

**Common mistake**
Tuning hyperparameters using your test set — this leaks test information into your model selection process, giving overly optimistic final performance estimates.""",
"quiz": """**Q1. What's a downside of grid search as hyperparameters increase?**  
A) None  B) The number of combinations to try grows exponentially, becoming very expensive  C) It becomes more accurate automatically  D) It stops working entirely  
**Answer: B**

**Q2. What does Optuna do differently from random search?**  
A) Nothing, they're identical  B) It uses past trial results to intelligently choose future hyperparameters to try  C) It only works on images  D) It doesn't require any code  
**Answer: B**

**Q3. Why shouldn't you tune hyperparameters directly on your test set?**  
A) It's fine to do so  B) It leaks test information into model selection, inflating your final performance estimate  C) Test sets are too small always  D) It makes training slower  
**Answer: B**"""
},

"Reproducible Pipelines": {
"explain": "Making sure a training run can be exactly repeated: managing configs cleanly, controlling random seeds, and generating clear reports of what happened.",
"teach": """**What it is**
Reproducible pipelines combine config management (keeping all settings in one trackable place), seed control (fixing randomness), and experiment reports (clear records of what ran and what resulted).

**Why it matters**
"I can't reproduce the result I got last week" is one of the most common and most avoidable failures in ML engineering.

**How it works**
Config files (YAML/JSON) centralize all settings instead of scattering magic numbers through code. Setting a fixed random seed (`torch.manual_seed(42)`, etc.) makes stochastic processes (weight init, data shuffling) deterministic and repeatable. Combined with data versioning and experiment tracking, this means any past run can be recreated exactly.

**Common mistake**
Assuming a fixed seed guarantees full determinism — some GPU operations remain non-deterministic by default unless you explicitly configure deterministic algorithms too.""",
"quiz": """**Q1. What's the purpose of setting a random seed?**  
A) To speed up training  B) To make stochastic processes repeatable across runs  C) To improve model accuracy  D) To reduce memory usage  
**Answer: B**

**Q2. Why use a config file instead of hardcoding settings in code?**  
A) It's not necessary  B) It centralizes and tracks all settings, making experiments easier to reproduce and compare  C) It makes code run faster  D) Config files are required by Python  
**Answer: B**

**Q3. Is setting a random seed alone always enough for full reproducibility on GPU?**  
A) Yes, always  B) Not necessarily — some GPU operations are non-deterministic unless explicitly configured otherwise  C) Seeds don't matter on GPU  D) GPUs ignore seeds entirely  
**Answer: B**"""
},

"CI Fundamentals": {
"explain": "Automatically testing and checking code every time it changes, using tools like GitHub Actions, so bugs get caught before they reach production.",
"teach": """**What it is**
Continuous Integration (CI) automatically runs tests, linters, and formatters every time code is pushed, using tools like GitHub Actions.

**Why it matters**
Catching a broken pipeline or a failing test in an automated check, seconds after pushing, is far cheaper than discovering it after it's already deployed.

**How it works**
A CI config file (e.g., `.github/workflows/ci.yml`) defines triggers (like "on every push") and steps (install dependencies, run tests, run a linter). If any step fails, the pipeline reports a failure, often blocking a merge until it's fixed.

**Common mistake**
Having CI but no actual tests to run — the automation is only as useful as what it's checking.""",
"quiz": """**Q1. What does Continuous Integration primarily automate?**  
A) Deploying to production  B) Running tests/checks automatically on every code change  C) Writing code for you  D) Managing databases  
**Answer: B**

**Q2. What typically happens if a CI check fails?**  
A) Nothing, it's just informational  B) It flags the failure, often blocking a merge until fixed  C) It automatically fixes the bug  D) It deletes the branch  
**Answer: B**

**Q3. What's the risk of setting up CI without writing real tests?**  
A) None  B) The automation has nothing meaningful to check, giving false confidence  C) CI won't run at all  D) It makes deployment impossible  
**Answer: B**"""
},

"CD for ML Models": {
"explain": "Automating what happens after training: triggering retraining when needed, and gating deployment behind validation checks so a worse model never silently replaces a better one.",
"teach": """**What it is**
Continuous Deployment (CD) for ML automates retraining triggers (e.g., on a schedule, or when drift is detected) and validation gates (only deploying a new model if it passes quality checks).

**Why it matters**
Without gates, an automated pipeline could silently deploy a broken or worse-performing model straight to production.

**How it works**
A retraining trigger kicks off the pipeline (new data available, scheduled interval, or detected drift). Before deployment, the new model is validated against a held-out set and compared to the current production model — only promoted if it meets a bar (e.g., "must not regress accuracy by more than X%").

**Common mistake**
Automatically deploying every retrained model with no comparison against the current production model's performance.""",
"quiz": """**Q1. What is a "validation gate" in ML CD?**  
A) A firewall rule  B) A quality check a new model must pass before being deployed  C) A type of database  D) A Docker command  
**Answer: B**

**Q2. What might trigger automated retraining?**  
A) Nothing, it's always manual  B) A schedule, new data, or detected drift  C) Only a developer's mood  D) A CSS change  
**Answer: B**

**Q3. Why compare a newly trained model against the current production model before deploying?**  
A) It's unnecessary  B) To ensure the new model doesn't silently perform worse  C) To slow down deployment intentionally  D) To increase costs  
**Answer: B**"""
},

"Testing ML Code": {
"explain": "Applying real software testing practices to ML pipelines: unit tests for individual functions, data validation tests for input assumptions, and integration tests for the whole pipeline.",
"teach": """**What it is**
Testing ML code means unit tests (checking individual functions), data validation tests (checking incoming data meets expected assumptions), and integration tests (checking the full pipeline works end-to-end).

**Why it matters**
ML pipelines fail in ways regular software often doesn't — silently, through bad data, rather than loudly, through a crash. Tests catch this early.

**How it works**
A unit test might check that a preprocessing function handles missing values correctly. A data validation test checks incoming data types, ranges, and null rates match expectations (e.g., using a tool like Great Expectations). An integration test runs the whole pipeline on a small sample end-to-end and checks it produces valid output.

**Common mistake**
Testing only model accuracy and skipping data validation — a pipeline can run "successfully" while silently training on corrupted or shifted data.""",
"quiz": """**Q1. What does a data validation test check?**  
A) Model accuracy only  B) That incoming data matches expected types, ranges, and quality  C) Server uptime  D) Code style only  
**Answer: B**

**Q2. Why are ML pipelines especially prone to silent failures?**  
A) They aren't  B) Bad data can produce a technically "successful" run with wrong results, with no crash  C) Python doesn't support error handling  D) All ML pipelines use the same data  
**Answer: B**

**Q3. What does an integration test verify?**  
A) A single function in isolation  B) That the full pipeline works correctly end-to-end  C) Only the UI  D) Only the database schema  
**Answer: B**"""
},

"Monitoring Basics": {
"explain": "Keeping visibility into a running system: logging and metrics for what's happening, dashboards (like Grafana) to see it, and alerting to know when something's wrong.",
"teach": """**What it is**
Monitoring covers logging (recording events), metrics (numeric measurements over time), dashboards (visualizing those metrics, e.g., in Grafana), and alerting (automatically notifying someone when something looks wrong).

**Why it matters**
A model can silently degrade in production for weeks without anyone noticing, unless something is actively watching key numbers and flagging problems.

**How it works**
Logs capture discrete events (a request came in, an error occurred). Metrics track numeric trends (requests per second, average latency, prediction distribution). A dashboard visualizes these over time; alerting rules (e.g., "latency > 2s for 5 minutes") automatically page someone when thresholds are crossed.

**Common mistake**
Setting up dashboards but no alerting — nobody stares at dashboards 24/7, so problems still go unnoticed without automated alerts.""",
"quiz": """**Q1. What's the difference between a log and a metric?**  
A) No difference  B) Logs record discrete events; metrics track numeric trends over time  C) Metrics are for images only  D) Logs are only for errors  
**Answer: B**

**Q2. What is the purpose of alerting?**  
A) To replace dashboards  B) To automatically notify someone when a metric crosses a concerning threshold  C) To slow down the system  D) To log every request  
**Answer: B**

**Q3. Why is a dashboard alone often insufficient?**  
A) It's always sufficient  B) Nobody watches it continuously, so problems can go unnoticed without alerts  C) Dashboards can't show numbers  D) They're too expensive to build  
**Answer: B**"""
},

"Data Drift": {
"explain": "When the statistical properties of incoming data change over time (covariate shift), silently making a model's assumptions stale — detected with tools like PSI and KS tests.",
"teach": """**What it is**
Data drift is when the distribution of input data changes over time compared to what the model was trained on (covariate shift), even if the true underlying relationship hasn't changed. PSI and KS tests are statistical tools to detect this.

**Why it matters**
A model trained on last year's customer behavior can quietly become inaccurate as customer behavior shifts — without drift monitoring, you'd only notice once performance visibly tanks.

**How it works**
The Population Stability Index (PSI) compares the distribution of a feature between training time and now, flagging significant shifts. The Kolmogorov-Smirnov (KS) test statistically compares two distributions to see if they likely come from the same underlying population. Both give an early warning system before a full performance drop happens.

**Common mistake**
Only monitoring model outputs and never the input feature distributions — by the time output-based metrics catch a problem, real damage may already be done.""",
"quiz": """**Q1. What is covariate shift?**  
A) A change in model architecture  B) A change in the distribution of input features over time  C) A type of neural network layer  D) A Docker command  
**Answer: B**

**Q2. What does the PSI metric help detect?**  
A) Code bugs  B) Significant shifts in a feature's distribution compared to training time  C) GPU memory usage  D) API latency  
**Answer: B**

**Q3. Why monitor input feature distributions, not just model output accuracy?**  
A) It's unnecessary  B) It gives an earlier warning before performance visibly degrades  C) Inputs never change  D) Outputs are always more informative  
**Answer: B**"""
},

"Model Drift": {
"explain": "When the relationship between inputs and the correct output changes over time (concept drift) — tracked by monitoring performance decay and used to trigger retraining.",
"teach": """**What it is**
Model drift (concept drift) is when the actual relationship between input and target changes — the model's learned patterns become outdated even if input distributions look stable.

**Why it matters**
Unlike data drift, concept drift means the "ground truth" itself has shifted (e.g., fraud patterns evolve as fraudsters adapt) — no amount of clean input data alone fixes this.

**How it works**
Performance decay tracking watches accuracy/precision/recall over time (where ground-truth labels become available, even delayed) to detect a real drop, not just an input shift. This feeds retraining triggers — deciding when accumulated drift justifies retraining the model on fresher data.

**Common mistake**
Confusing data drift and concept drift — they require different responses: data drift might just need feature recalibration, while concept drift usually requires retraining on new labeled data.""",
"quiz": """**Q1. What distinguishes concept drift from data drift?**  
A) They're identical  B) Concept drift is a change in the input-output relationship itself, not just input distribution  C) Concept drift only affects images  D) Data drift is more severe always  
**Answer: B**

**Q2. Why might a fraud detection model experience concept drift specifically?**  
A) It never does  B) Fraud patterns evolve as fraudsters adapt, changing what "fraud" looks like  C) Fraud data never changes  D) It's unrelated to fraud detection  
**Answer: B**

**Q3. What's the typical response to significant concept drift?**  
A) Ignore it  B) Retrain the model on fresher, more representative data  C) Delete the model  D) Change the programming language  
**Answer: B**"""
},

"Observability": {
"explain": "Deeper visibility into a running system beyond basic monitoring: tracing individual requests end-to-end, tracking error budgets, and having a real incident response process.",
"teach": """**What it is**
Observability extends monitoring with request tracing (following a single request across every service it touches), error budgets (a formal allowance for how much failure is acceptable), and incident response processes (what happens when something breaks).

**Why it matters**
When a request is slow, monitoring tells you "something's slow somewhere" — tracing tells you exactly which step in the pipeline is the bottleneck.

**How it works**
Tracing tags a request with a unique ID as it flows through your system, timing each stage, so you can see exactly where time is spent. An error budget (e.g., "99.9% uptime allowed, meaning ~43 minutes of downtime per month") formalizes acceptable risk, guiding how cautious to be about releases. Incident response defines clear steps: detect, triage, mitigate, resolve, and do a retrospective afterward.

**Common mistake**
Having no error budget and treating every single failure as equally unacceptable — this either causes burnout from overreacting, or masks genuinely serious issues among noise.""",
"quiz": """**Q1. What does request tracing help you identify?**  
A) Total server cost  B) Exactly which stage in a multi-step pipeline is slow or failing  C) The programming language used  D) The number of users  
**Answer: B**

**Q2. What is an error budget?**  
A) A financial budget for errors  B) A formal allowance for how much failure/downtime is acceptable  C) A type of unit test  D) A Docker configuration file  
**Answer: B**

**Q3. What's a key part of good incident response?**  
A) Ignoring the issue until it resolves itself  B) A clear process: detect, triage, mitigate, resolve, and retrospective  C) Immediately deleting the affected service  D) Blaming a specific engineer  
**Answer: B**"""
},

"Model Serving Basics": {
"explain": "The fundamental choice in deploying models: exposing predictions through a REST API in real-time, versus running predictions in bulk on a schedule (batch inference).",
"teach": """**What it is**
Model serving is how a trained model actually delivers predictions to users or systems — either via a REST API responding in real-time, or via batch inference processing many records at once on a schedule.

**Why it matters**
Choosing the wrong pattern wastes resources: real-time serving for something that could run overnight in batch is unnecessarily expensive and complex.

**How it works**
A REST API (e.g., FastAPI) exposes an endpoint that accepts input and returns a prediction within milliseconds to seconds — good for interactive use cases (like a chatbot). Batch inference processes a large dataset all at once, on a schedule, and stores results for later use — good for things like nightly recommendation updates where instant response isn't needed.

**Common mistake**
Building real-time serving infrastructure for a use case that only ever needs daily batch predictions — massively overengineering the solution.""",
"quiz": """**Q1. When is batch inference typically preferred over real-time serving?**  
A) When users need instant predictions  B) When predictions can be computed on a schedule without needing instant response  C) Never, real-time is always better  D) Only for image data  
**Answer: B**

**Q2. What does a REST API for model serving typically expose?**  
A) A database connection  B) An endpoint that accepts input and returns a prediction  C) A file download only  D) A training script  
**Answer: B**

**Q3. What's a risk of overusing real-time serving?**  
A) None  B) Unnecessary infrastructure complexity and cost for use cases that don't need instant response  C) It's always the cheaper option  D) It removes the need for a trained model  
**Answer: B**"""
},

"Scalable Serving": {
"explain": "Handling growing traffic to a model API: load balancing across multiple instances, horizontal scaling (adding more instances), and caching repeated requests.",
"teach": """**What it is**
Scalable serving covers load balancing (distributing requests across multiple model instances), horizontal scaling (adding more instances as demand grows), and caching (avoiding recomputation for repeated/identical requests).

**Why it matters**
A single model instance has a hard ceiling on how many requests per second it can handle — scaling patterns are what let a service handle real-world traffic spikes without falling over.

**How it works**
A load balancer sits in front of multiple identical model server instances, routing each incoming request to one of them (e.g., round-robin). Horizontal scaling adds more instances behind that load balancer as traffic grows (versus vertical scaling, which just makes one instance bigger). Caching stores results for repeated identical inputs, skipping the expensive model call entirely on a cache hit.

**Common mistake**
Scaling vertically (bigger machine) indefinitely instead of horizontally — vertical scaling has hard limits and a single point of failure; horizontal scaling doesn't.""",
"quiz": """**Q1. What does a load balancer do?**  
A) Trains the model  B) Distributes incoming requests across multiple server instances  C) Stores data permanently  D) Writes logs only  
**Answer: B**

**Q2. What's the difference between horizontal and vertical scaling?**  
A) No difference  B) Horizontal adds more instances; vertical makes one instance bigger  C) Vertical is always better  D) Horizontal only applies to databases  
**Answer: B**

**Q3. When does caching help most in model serving?**  
A) When every request is unique  B) When identical or very similar requests repeat often  C) It never helps  D) Only for training, not serving  
**Answer: B**"""
},

"Serving Frameworks": {
"explain": "Purpose-built tools for serving models efficiently in production: TorchServe/TF Serving for framework-native deployment, ONNX Runtime for cross-framework portability, and Triton for high-performance multi-model serving.",
"teach": """**What it is**
Serving frameworks are specialized infrastructure for running models in production efficiently: TorchServe/TF Serving (framework-native model servers), ONNX Runtime (a portable format/runtime that works across frameworks), and Triton Inference Server (NVIDIA's high-performance server supporting many frameworks and models at once).

**Why it matters**
Hand-rolling a FastAPI wrapper works for simple cases, but purpose-built serving frameworks add batching, GPU optimization, and multi-model management that would take significant effort to build yourself.

**How it works**
TorchServe/TF Serving are optimized specifically for their respective frameworks' model formats. ONNX (Open Neural Network Exchange) is a common format you can export a model to from many frameworks, then run anywhere ONNX Runtime is supported — decoupling training framework from serving environment. Triton can serve multiple different models (even from different frameworks) simultaneously, with automatic request batching for efficiency.

**Common mistake**
Assuming a hand-rolled FastAPI server will scale as well as a purpose-built serving framework — they lack the automatic batching and hardware-level optimizations these tools provide.""",
"quiz": """**Q1. What is ONNX primarily used for?**  
A) Training models  B) A portable format so models can run across different frameworks/runtimes  C) Writing Dockerfiles  D) Data visualization  
**Answer: B**

**Q2. What's an advantage of Triton Inference Server?**  
A) It only supports one framework  B) It can serve multiple models/frameworks simultaneously with optimizations like batching  C) It replaces the need for GPUs  D) It's only for training  
**Answer: B**

**Q3. Why might a hand-rolled FastAPI model server underperform a dedicated serving framework?**  
A) FastAPI is broken  B) Dedicated frameworks add optimizations like automatic batching and hardware-specific tuning  C) There's no real difference  D) FastAPI can't return JSON  
**Answer: B**"""
},

"Cost & Latency Optimization": {
"explain": "Making model inference cheaper and faster: quantization shrinks model size/precision, batching processes multiple requests together, and autoscaling matches resources to actual demand.",
"teach": """**What it is**
Optimizing serving means reducing cost and latency: quantization (using lower-precision numbers to shrink models), batching requests together, and autoscaling (automatically adjusting the number of running instances to match demand).

**Why it matters**
Inference cost, not training cost, is usually the dominant long-term expense for a deployed ML system that serves lots of traffic — small optimizations here compound significantly.

**How it works**
Quantization converts model weights from 32-bit floats to lower precision (like 8-bit integers), shrinking model size and speeding up inference with a small, usually acceptable, accuracy tradeoff. Batching groups several incoming requests into one forward pass through the model, using hardware more efficiently than processing them one at a time. Autoscaling watches traffic/load metrics and spins instances up or down automatically, avoiding both overprovisioning (wasted cost) and underprovisioning (slow/failed requests).

**Common mistake**
Running a fixed number of instances sized for peak traffic 24/7 instead of autoscaling — this means paying for peak capacity even during quiet periods.""",
"quiz": """**Q1. What does quantization typically trade off?**  
A) Nothing, it's free  B) A small amount of accuracy for reduced model size and faster inference  C) Training data quality  D) Model interpretability  
**Answer: B**

**Q2. Why is batching requests together more efficient?**  
A) It isn't  B) It uses hardware (especially GPUs) more efficiently than processing one request at a time  C) It reduces model accuracy on purpose  D) It only works for text data  
**Answer: B**

**Q3. What problem does autoscaling solve?**  
A) Model accuracy issues  B) Matching running capacity to actual traffic, avoiding both overpaying and underprovisioning  C) Data versioning  D) Code formatting  
**Answer: B**"""
},

# ---------------- AI Engineer phase ----------------

"Transformer Architecture": {
"explain": "The architecture behind virtually every modern LLM: self-attention lets every token directly weigh every other token, and positional encoding tells the model the order of tokens.",
"teach": """**What it is**
The Transformer architecture relies on self-attention (each token computes how much to "attend to" every other token) and positional encoding (injecting order information, since attention itself has no inherent sense of sequence order).

**Why it matters**
This architecture replaced RNNs for most language tasks because it processes all tokens in parallel (much faster to train) and directly connects distant tokens (no vanishing gradient over long sequences).

**How it works**
For each token, self-attention computes a Query, Key, and Value vector; the similarity between a token's Query and every other token's Key determines how much of each token's Value gets blended into the output — effectively letting the model decide "which other words matter for understanding this one." Positional encoding adds a pattern (often sinusoidal) representing each token's position, since without it, "dog bites man" and "man bites dog" would look identical to pure attention.

**Common mistake**
Thinking attention "understands" language the way humans do — it's a powerful pattern-matching mechanism, not comprehension in a human sense.""",
"quiz": """**Q1. What does self-attention let each token do?**  
A) Ignore all other tokens  B) Weigh the relevance of every other token when building its representation  C) Only look at the previous token  D) Randomly select a token  
**Answer: B**

**Q2. Why is positional encoding needed?**  
A) It isn't needed  B) Attention alone has no built-in sense of token order  C) It speeds up training only  D) It reduces model size  
**Answer: B**

**Q3. Why did Transformers largely replace RNNs for language tasks?**  
A) They're smaller  B) They parallelize training and connect distant tokens directly, avoiding RNN's sequential bottleneck  C) They don't need any training data  D) RNNs were banned  
**Answer: B**"""
},

"Tokenization & Embeddings": {
"explain": "How text becomes numbers a model can process: tokenization (like BPE) splits text into sub-word pieces, and embeddings turn each token into a vector capturing meaning.",
"teach": """**What it is**
Tokenization splits raw text into smaller units (often sub-word pieces via Byte-Pair Encoding, or BPE); embeddings map each token to a dense numeric vector that captures some notion of meaning, where similar words end up as similar vectors.

**Why it matters**
Every LLM interaction starts here — how text gets chopped into tokens directly affects cost (you're billed per token) and even model behavior on rare words or unusual formatting.

**How it works**
BPE starts with individual characters and iteratively merges the most frequent adjacent pairs into new sub-word units, letting common words become single tokens while rare words get split into meaningful pieces. Each resulting token is then mapped to a learned embedding vector; vector similarity (like cosine similarity) between embeddings approximates semantic similarity between words/tokens.

**Common mistake**
Assuming tokens correspond to whole words — many tokens are sub-word fragments, which is why LLMs sometimes struggle with exact character counting or spelling tasks.""",
"quiz": """**Q1. What does Byte-Pair Encoding (BPE) do?**  
A) Encrypts text  B) Iteratively merges frequent character/sub-word pairs into tokens  C) Translates languages  D) Removes punctuation  
**Answer: B**

**Q2. What does an embedding vector aim to capture?**  
A) The exact spelling of a word  B) Some notion of a token's meaning, so similar tokens have similar vectors  C) The token's file size  D) Random noise  
**Answer: B**

**Q3. Why do LLMs sometimes struggle with exact character counting?**  
A) They're broken  B) Tokens are often sub-word fragments, not individual characters  C) They can't process numbers  D) It's a training data issue only  
**Answer: B**"""
},

"Pretraining & Fine-tuning": {
"explain": "How LLMs are built in two stages: pretraining on massive general text to learn language broadly, then fine-tuning (including efficient methods like LoRA/QLoRA) to specialize on a specific task.",
"teach": """**What it is**
Pretraining trains a model on huge amounts of general text (predicting the next token) to build broad language ability. Fine-tuning then adapts that pretrained model to a specific task or style, often using efficient methods like LoRA/QLoRA that update only a small number of additional parameters.

**Why it matters**
Pretraining is enormously expensive (millions of dollars for frontier models) — fine-tuning lets you leverage that investment cheaply, adapting a general model to your specific need without retraining from scratch.

**How it works**
Pretraining objectives are typically self-supervised (like "predict the next token"), needing no manual labels — the text itself provides the training signal. LoRA (Low-Rank Adaptation) freezes the original model weights and injects small trainable low-rank matrices, dramatically reducing the number of parameters that need updating during fine-tuning, which also reduces memory and compute needs. QLoRA further combines this with quantizing the frozen base model to save even more memory.

**Common mistake**
Fine-tuning an LLM when a well-crafted prompt (covered in Prompt Engineering) would have solved the problem for far less effort and cost.""",
"quiz": """**Q1. What is the typical pretraining objective for LLMs?**  
A) Classifying images  B) Predicting the next token in text (self-supervised)  C) Playing games  D) Sorting numbers  
**Answer: B**

**Q2. What does LoRA do during fine-tuning?**  
A) Retrains the entire model from scratch  B) Freezes original weights and trains small added low-rank matrices instead  C) Deletes the base model  D) Only works on images  
**Answer: B**

**Q3. Before fine-tuning, what's often worth trying first?**  
A) Buying more GPUs  B) A well-crafted prompt, which can solve many tasks without any training  C) Deleting the training data  D) Nothing, always fine-tune first  
**Answer: B**"""
},

"LLM Evaluation": {
"explain": "How you actually judge if an LLM (or a prompt/fine-tune) is good: perplexity as an intrinsic metric, benchmark suites for standardized comparison, and human evaluation for what automated metrics miss.",
"teach": """**What it is**
LLM evaluation includes perplexity (a measure of how "surprised" a model is by real text — lower is better), benchmark suites (standardized test sets covering reasoning, knowledge, coding, etc.), and human evaluation (people directly judging output quality).

**Why it matters**
A model can score well on an automated benchmark while still producing outputs that feel unhelpful or wrong to actual users — evaluation needs multiple angles, not just one number.

**How it works**
Perplexity measures how well a model predicts held-out text — mathematically related to the model's average token-level uncertainty. Benchmark suites (like MMLU, HellaSwag, HumanEval) run a model against thousands of standardized questions for comparable scores across models. Human evaluation (or LLM-as-judge, using a strong model to grade another's output) is often needed for aspects benchmarks don't capture well, like tone, helpfulness, or nuanced correctness.

**Common mistake**
Relying solely on benchmark leaderboard numbers to pick a model for your specific use case — benchmarks measure general capability, not necessarily performance on your particular task.""",
"quiz": """**Q1. What does a lower perplexity score generally indicate?**  
A) A worse model  B) A model less "surprised" by real text, generally indicating better language modeling  C) Faster inference only  D) Nothing meaningful  
**Answer: B**

**Q2. Why use human evaluation in addition to benchmarks?**  
A) Benchmarks are always sufficient  B) Benchmarks may miss qualities like helpfulness, tone, or nuanced correctness  C) Human evaluation is faster  D) It's required by law  
**Answer: B**

**Q3. What's a risk of picking a model purely by benchmark leaderboard rank?**  
A) None  B) General benchmark performance may not reflect performance on your specific use case  C) Benchmarks are always task-specific  D) Leaderboards are never public  
**Answer: B**"""
},

"Prompt Engineering": {
"explain": "Getting better outputs from an LLM through how you ask: zero/few-shot examples, chain-of-thought reasoning prompts, and reusable prompt templates.",
"teach": """**What it is**
Prompt engineering is the practice of structuring your input to an LLM for better results — zero-shot (no examples), few-shot (a handful of examples in the prompt), chain-of-thought (asking the model to reason step-by-step), and templates (reusable, parameterized prompt structures).

**Why it matters**
The exact same underlying model can go from unreliable to consistently accurate purely based on how the request is phrased — often far cheaper than fine-tuning.

**How it works**
Few-shot prompting shows the model a couple of example input-output pairs before the real question, letting it infer the expected pattern. Chain-of-thought prompting (e.g., "think step by step") encourages the model to show intermediate reasoning, which often improves accuracy on complex problems by giving it "room to think" in its own output before committing to a final answer.

**Common mistake**
Writing vague, ambiguous prompts and blaming the model for inconsistent outputs — specificity and clear structure in the prompt usually fixes this.""",
"quiz": """**Q1. What is few-shot prompting?**  
A) Asking with zero context  B) Providing a few example input-output pairs in the prompt  C) Fine-tuning the model  D) Reducing the model's size  
**Answer: B**

**Q2. Why does chain-of-thought prompting often improve accuracy?**  
A) It shortens the response  B) It gives the model room to reason step-by-step before the final answer  C) It reduces token usage  D) It bypasses the model's training  
**Answer: B**

**Q3. What's usually the cheaper first fix for inconsistent LLM output — fine-tuning or better prompting?**  
A) Fine-tuning  B) Better, more specific prompting  C) Neither helps  D) Buying a bigger model always  
**Answer: B**"""
},

"Embeddings & Vector Search": {
"explain": "Turning text (or other data) into vectors that capture meaning, storing them in a vector database, and finding the most similar items via similarity search — the foundation of retrieval and RAG.",
"teach": """**What it is**
Embedding models convert text into dense vectors capturing semantic meaning. Vector databases store these efficiently at scale. Similarity search finds the closest vectors to a query, which correspond to the most semantically similar content.

**Why it matters**
This is the retrieval backbone behind RAG, semantic search, and recommendation systems — letting you find "similar meaning," not just "matching keywords."

**How it works**
An embedding model maps a piece of text to a fixed-length vector such that semantically similar texts end up close together in that vector space. A vector database (like Pinecone, Weaviate, or pgvector) indexes millions of these vectors for fast approximate nearest-neighbor search. A query gets embedded the same way, then the database returns the stored vectors closest to it (via cosine similarity or similar metrics).

**Common mistake**
Embedding queries and documents with two different, incompatible embedding models — vectors from different models aren't comparable to each other.""",
"quiz": """**Q1. What does an embedding model output for a piece of text?**  
A) A shorter version of the text  B) A dense numeric vector capturing semantic meaning  C) A translated version  D) A random ID  
**Answer: B**

**Q2. What is a vector database optimized for?**  
A) Storing plain text only  B) Fast similarity search over large numbers of vectors  C) Running training jobs  D) Sending emails  
**Answer: B**

**Q3. Why is it a problem to embed queries and documents with different embedding models?**  
A) It isn't a problem  B) Vectors from different models aren't in the same space and aren't meaningfully comparable  C) It saves money  D) It always improves accuracy  
**Answer: B**"""
},

"RAG Fundamentals": {
"explain": "Retrieval-Augmented Generation: retrieving relevant documents (chunked and ranked) and feeding them to an LLM as context, so it can answer using information beyond its training data.",
"teach": """**What it is**
RAG combines retrieval (finding relevant chunks of information via vector search) with generation (an LLM producing an answer using that retrieved context). Chunking splits documents into manageable pieces; reranking further sorts retrieved results by relevance before feeding the best ones to the model.

**Why it matters**
RAG lets an LLM answer questions about your private documents, recent events, or specialized knowledge — without expensive retraining or fine-tuning.

**How it works**
Documents are split into chunks (e.g., a few hundred words each), embedded, and stored in a vector database. At query time, the user's question is embedded and used to retrieve the most similar chunks. Those chunks are inserted into the LLM's prompt as context, and the model generates an answer grounded in that retrieved information. A reranker (often a separate smaller model) can reorder initial retrieval results for better precision before this final step.

**Common mistake**
Using chunks that are too large or too small — too large wastes context and dilutes relevance; too small loses necessary surrounding context for the model to make sense of the retrieved snippet.""",
"quiz": """**Q1. What does the "retrieval" step in RAG do?**  
A) Trains a new model  B) Finds relevant chunks of information via similarity search  C) Generates the final answer directly  D) Deletes irrelevant documents  
**Answer: B**

**Q2. Why chunk documents before embedding them?**  
A) It's not necessary  B) To create manageable, retrievable pieces rather than embedding entire huge documents at once  C) To make files smaller on disk  D) To translate them  
**Answer: B**

**Q3. What does a reranker do in a RAG pipeline?**  
A) Generates the final text  B) Reorders initially retrieved chunks by relevance for better precision  C) Trains the embedding model  D) Chunks the documents  
**Answer: B**"""
},

"Advanced RAG": {
"explain": "Improving on basic RAG: hybrid search combines keyword and semantic search, query rewriting improves the search query itself, and multi-hop retrieval chains multiple retrieval steps for complex questions.",
"teach": """**What it is**
Advanced RAG techniques address basic RAG's limitations: hybrid search (combining keyword/BM25 search with semantic vector search), query rewriting (transforming a user's raw question into a better search query), and multi-hop retrieval (chaining several retrieval steps to answer questions that require connecting multiple pieces of information).

**Why it matters**
Basic single-shot vector retrieval fails on queries needing exact terms (like product codes) or questions that require combining facts from multiple separate documents.

**How it works**
Hybrid search runs both a keyword-based search (good for exact matches) and a semantic search (good for meaning-based matches), then combines/reranks both result sets. Query rewriting might expand an ambiguous question or break it into sub-questions before retrieval. Multi-hop retrieval performs an initial retrieval, uses that result to inform a second retrieval query, and repeats as needed — useful for "what's the capital of the country where X was born?"-style questions.

**Common mistake**
Assuming pure semantic (vector) search alone is always sufficient — it often misses exact keyword matches like IDs, codes, or names that hybrid search would catch.""",
"quiz": """**Q1. What does hybrid search combine?**  
A) Two LLMs  B) Keyword-based search and semantic vector search  C) Two vector databases  D) Training and inference  
**Answer: B**

**Q2. Why is multi-hop retrieval needed for some questions?**  
A) It isn't, single retrieval always works  B) Some questions require combining facts found across multiple separate retrieval steps  C) It only applies to images  D) It replaces the need for an LLM  
**Answer: B**

**Q3. What's a limitation of pure semantic vector search alone?**  
A) None  B) It can miss exact keyword/ID matches that a keyword search would catch  C) It's always slower than keyword search  D) It can't be combined with anything else  
**Answer: B**"""
},

"Agents": {
"explain": "LLMs that can take actions, not just generate text: calling external tools/functions, reasoning step-by-step with the ReAct pattern, and coordinating multiple specialized agents together.",
"teach": """**What it is**
Agents extend LLMs beyond text generation into taking actions: tool use/function calling (the model requests a specific function be run, like a web search or calculator), the ReAct pattern (interleaving Reasoning and Acting in a loop), and multi-agent systems (multiple specialized agents collaborating on a task).

**Why it matters**
Pure text generation can't check today's weather, run code, or query a database — tool use is what lets an LLM-based system actually interact with the real world and take useful actions.

**How it works**
Function calling lets you define available tools (with names, descriptions, and expected arguments); the model decides when to invoke one, your code executes it, and the result is fed back into the conversation for the model to use. ReAct loops this: the model reasons about what to do, acts (calls a tool), observes the result, and repeats until it has enough information to answer. Multi-agent systems assign different roles (e.g., a "researcher" agent and a "writer" agent) that pass work between each other.

**Common mistake**
Giving an agent too many overlapping tools with unclear descriptions — the model frequently picks the wrong tool or gets stuck when tool boundaries are ambiguous.""",
"quiz": """**Q1. What does function calling let an LLM do?**  
A) Directly execute code itself  B) Request that your code run a specific function, then use the result  C) Train itself further  D) Access the internet directly without any code  
**Answer: B**

**Q2. What does the ReAct pattern interleave?**  
A) Training and testing  B) Reasoning and Acting, in a repeated loop  C) Two different LLMs  D) Encoding and decoding  
**Answer: B**

**Q3. Why can too many overlapping tools hurt an agent's performance?**  
A) It never hurts  B) The model can pick the wrong tool or get confused about ambiguous boundaries between them  C) It always speeds things up  D) Tools don't affect model behavior  
**Answer: B**"""
},

"Serving LLM Apps": {
"explain": "The engineering specifics of putting an LLM-powered app into production: building the API layer (often FastAPI), streaming partial responses, and handling many concurrent requests asynchronously.",
"teach": """**What it is**
Serving LLM apps involves building an API (commonly FastAPI) around your LLM calls, streaming responses token-by-token as they're generated (rather than waiting for the full response), and async handling to serve many concurrent users efficiently.

**Why it matters**
LLM calls are slow (seconds, not milliseconds) — without streaming and async handling, your app either feels sluggish or falls over under concurrent load.

**How it works**
Streaming sends each token to the client as soon as it's generated, so users see text appearing progressively instead of staring at a blank screen for several seconds. Async handling (Python's `async`/`await`) lets your server start processing another request while waiting on a slow LLM API call, rather than blocking entirely on one request at a time.

**Common mistake**
Writing LLM API calls synchronously in a web server that needs to handle multiple concurrent users — this serializes all requests behind each other, making the app feel unnecessarily slow under any real load.""",
"quiz": """**Q1. What does streaming responses primarily improve?**  
A) Model accuracy  B) Perceived responsiveness, since users see output as it's generated  C) Training speed  D) Data storage  
**Answer: B**

**Q2. Why does async handling matter for LLM app servers?**  
A) It doesn't matter  B) It lets the server handle other requests while waiting on slow LLM calls, instead of blocking  C) It makes the model smarter  D) It reduces token costs directly  
**Answer: B**

**Q3. What happens if LLM calls are handled synchronously under concurrent load?**  
A) Nothing changes  B) Requests get serialized behind each other, making the app feel slow  C) It automatically scales  D) It reduces costs  
**Answer: B**"""
},

"LLM Ops": {
"explain": "Operational practices specific to running LLM-powered features: prompt versioning, tracking API costs, and optimizing latency — the MLOps equivalent for LLM applications.",
"teach": """**What it is**
LLM Ops covers prompt versioning (tracking changes to prompts like code), cost tracking (LLM API calls are billed per token and can add up fast), and latency optimization (making responses feel fast despite inherently slow generation).

**Why it matters**
A small prompt tweak can silently change your app's behavior for every user — without versioning, you lose the ability to know what changed or roll back a regression.

**How it works**
Prompt versioning treats prompts like code: stored in version control, tested before deployment, with clear diffs between versions. Cost tracking logs token usage per request (input + output tokens, since both are billed) to catch runaway costs early. Latency optimization techniques include streaming, using smaller/faster models where quality allows, and caching common queries.

**Common mistake**
Editing prompts directly in production code with no tracking or testing — this makes it nearly impossible to know which prompt version caused a quality regression.""",
"quiz": """**Q1. Why version prompts like code?**  
A) It's unnecessary  B) So you can track changes, test them, and roll back regressions  C) Prompts never change  D) It's required by the LLM provider  
**Answer: B**

**Q2. What is typically billed in an LLM API call?**  
A) Only output tokens  B) Both input and output tokens  C) Neither, it's free  D) Only the number of requests, not tokens  
**Answer: B**

**Q3. What's one common latency optimization technique for LLM apps?**  
A) Always using the largest available model  B) Streaming responses and/or using a smaller, faster model where acceptable  C) Removing all caching  D) Increasing max_tokens unnecessarily  
**Answer: B**"""
},

"Guardrails & Safety": {
"explain": "Keeping an LLM application's outputs safe and reliable: validating outputs before showing them to users, filtering harmful content, and rate limiting to prevent abuse.",
"teach": """**What it is**
Guardrails cover output validation (checking an LLM's response meets expected format/quality before using it), content filtering (blocking harmful or inappropriate outputs), and rate limiting (capping how many requests a user can make, to prevent abuse and control cost).

**Why it matters**
LLMs can hallucinate, produce malformed output, or occasionally generate inappropriate content — production apps need automated checks, not just hope, between the model and the user.

**How it works**
Output validation might check that a response is valid JSON (if that's expected), doesn't exceed a length limit, or doesn't contain banned phrases. Content filtering can use a separate moderation model/API to flag unsafe content before it reaches the user. Rate limiting tracks requests per user/API key over a time window and rejects requests beyond the configured limit.

**Common mistake**
Trusting an LLM's raw output directly in a downstream system (like executing generated code or inserting into a database query) without validation — this is a real security risk, not just a quality one.""",
"quiz": """**Q1. What does output validation check for?**  
A) Nothing important  B) That an LLM's response meets expected format, length, or quality before use  C) Only spelling errors  D) The user's identity  
**Answer: B**

**Q2. Why is rate limiting important for LLM apps?**  
A) It's not important  B) It prevents abuse and controls runaway API costs  C) It makes responses more accurate  D) It's only for security cameras  
**Answer: B**

**Q3. What's a real risk of using raw LLM output directly in a downstream system unchecked?**  
A) None  B) Security or correctness issues, like executing unsafe generated code or malformed queries  C) It always improves performance  D) It's the recommended best practice  
**Answer: B**"""
},

"Evaluation in Production": {
"explain": "Continuously checking LLM app quality after deployment: A/B testing different prompts, collecting user feedback, and logging/tracing to understand real-world behavior.",
"teach": """**What it is**
Production evaluation covers A/B testing prompts (comparing two prompt versions on real traffic), user feedback loops (collecting thumbs up/down or corrections from real users), and logging & tracing (recording what actually happened for later analysis).

**Why it matters**
Offline evaluation (benchmarks, test sets) can't capture everything real users will do — production evaluation catches issues and improvement opportunities that only show up at scale, with real usage patterns.

**How it works**
A/B testing routes a portion of real traffic to a new prompt/model version, comparing key metrics (satisfaction, task completion, cost) against the current version before fully rolling it out. User feedback loops (like a thumbs up/down button) give a direct, if noisy, signal about output quality. Logging captures full request/response pairs (respecting privacy) so you can later analyze failure patterns or build new fine-tuning/eval datasets from real usage.

**Common mistake**
Only evaluating a model offline before launch and never again — production evaluation is continuous, not a one-time gate before deployment.""",
"quiz": """**Q1. What does A/B testing prompts in production let you do?**  
A) Nothing measurable  B) Compare real-world performance of two prompt versions before fully committing to one  C) Train a new model  D) Skip evaluation entirely  
**Answer: B**

**Q2. Why are user feedback loops valuable, even if noisy?**  
A) They aren't valuable  B) They give a direct signal about real-world output quality that offline benchmarks can't fully capture  C) They replace the need for any other evaluation  D) They only work for images  
**Answer: B**

**Q3. Why is production evaluation described as continuous rather than one-time?**  
A) It isn't, one evaluation is enough  B) Real-world usage patterns and issues emerge over time, requiring ongoing monitoring  C) It's continuous only for cost reasons  D) Continuous evaluation is not possible with LLMs  
**Answer: B**"""
},

"Graph Neural Networks": {
"explain": "Neural networks designed for graph-structured data: message passing lets nodes share information with neighbors, GCNs/GATs are common architectures, and heterogeneous graphs handle multiple node/edge types.",
"teach": """**What it is**
GNNs operate on graph-structured data (nodes and edges) using message passing — each node updates its representation by aggregating information from its neighbors, repeated over several layers. GCNs and GATs are common GNN variants; heterogeneous graphs contain multiple distinct types of nodes and edges (e.g., users, products, and reviews all in one graph).

**Why it matters**
Many real problems are naturally graph-shaped — social networks, fraud rings, molecule structures, recommendation systems — where standard CNNs/RNNs don't naturally apply.

**How it works**
In message passing, each node collects information from its direct neighbors, combines it (e.g., via averaging or attention), and updates its own representation — after several layers, each node's representation reflects information from increasingly distant parts of the graph. Graph Attention Networks (GATs) add attention weights so a node can weigh some neighbors more heavily than others, similar in spirit to Transformer attention.

**Common mistake**
Using too many message-passing layers — nodes can end up with overly similar, "smoothed out" representations (a problem called over-smoothing), losing useful distinguishing information.""",
"quiz": """**Q1. What does message passing let each node do?**  
A) Ignore the rest of the graph  B) Aggregate information from its neighboring nodes to update its own representation  C) Delete edges  D) Train independently with no graph structure  
**Answer: B**

**Q2. What is a heterogeneous graph?**  
A) A graph with only one node type  B) A graph containing multiple distinct types of nodes and/or edges  C) A fully connected graph  D) A graph with no edges  
**Answer: B**

**Q3. What is "over-smoothing" in GNNs?**  
A) A training speed issue  B) Node representations becoming too similar after too many message-passing layers  C) A type of data augmentation  D) A GPU memory error  
**Answer: B**"""
},

"Physics-Informed ML": {
"explain": "Combining known physical laws with neural networks: PINNs bake physics equations into the loss function, and Neural ODEs model continuous dynamics, both used to build efficient simulation surrogates.",
"teach": """**What it is**
Physics-Informed Neural Networks (PINNs) incorporate known physical equations directly into a model's loss function, so it learns solutions that respect those laws. Neural ODEs model systems as continuous-time differential equations learned by a network. Both are used to build "surrogate" models — fast approximations of expensive physical simulations.

**Why it matters**
Traditional physical simulations (like fluid dynamics or N-body systems) can be extremely computationally expensive — a trained surrogate model can approximate results orders of magnitude faster once trained.

**How it works**
A PINN's loss function includes not just data-fitting error, but also a term penalizing violation of a known governing equation (like a PDE), so the network is nudged toward physically plausible solutions even with limited data. A Neural ODE parameterizes the derivative of a system's state as a neural network, letting you model continuous dynamics rather than discrete steps.

**Common mistake**
Expecting a physics-informed model to work well with zero physical knowledge baked in — the entire value proposition depends on correctly encoding the actual governing equations relevant to your problem.""",
"quiz": """**Q1. What makes a PINN different from a standard neural network?**  
A) It uses more layers  B) Its loss function includes a term enforcing known physical equations  C) It doesn't use gradient descent  D) It only works on images  
**Answer: B**

**Q2. What does a Neural ODE model?**  
A) A discrete classification problem  B) A system's dynamics as a continuous-time differential equation  C) A type of image filter  D) A database query  
**Answer: B**

**Q3. Why build a "surrogate" model for physical simulations?**  
A) To make the simulation slower  B) To approximate expensive simulations much faster once trained  C) Surrogates are always more accurate than the real simulation  D) There's no real benefit  
**Answer: B**"""
},

"Generative Models": {
"explain": "Models that create new data rather than just classifying it: VAEs learn a compressed latent representation to generate from, GANs pit a generator against a discriminator, and diffusion models generate by gradually denoising.",
"teach": """**What it is**
Generative models learn to produce new data resembling their training distribution. VAEs (Variational Autoencoders) learn a compressed latent space you can sample from. GANs (Generative Adversarial Networks) train a generator and discriminator against each other. Diffusion models generate by learning to reverse a gradual noising process.

**Why it matters**
This family of models powers image generation, synthetic data creation, and (via related ideas) parts of modern generative AI more broadly.

**How it works**
A VAE encodes input into a compressed latent distribution, then decodes samples from that distribution back into data space — the "variational" part ensures the latent space is smooth and sample-able. A GAN's generator tries to produce fake data realistic enough to fool a discriminator, while the discriminator tries to correctly tell real from fake — both improve through this competition. Diffusion models start from pure noise and iteratively denoise it, step by step, guided by a model trained to predict and remove noise at each stage.

**Common mistake**
Assuming GANs are always easier to train than alternatives — GAN training is notoriously unstable (mode collapse, oscillating losses) compared to VAEs or diffusion models.""",
"quiz": """**Q1. What do the generator and discriminator do in a GAN?**  
A) They cooperate directly on the same task  B) The generator creates fake data; the discriminator tries to distinguish real from fake, improving both through competition  C) They train completely independently with no interaction  D) Neither uses neural networks  
**Answer: B**

**Q2. How do diffusion models generate new data?**  
A) By directly copying training examples  B) By iteratively denoising a starting point of pure noise  C) By running a decision tree  D) By running k-NN  
**Answer: B**

**Q3. What is a known challenge with training GANs?**  
A) They're always stable  B) Training instability, such as mode collapse  C) They require no data  D) They can't generate images  
**Answer: B**"""
},

"Federated & Efficient Learning": {
"explain": "Training and running models efficiently at scale: federated learning trains across decentralized devices without centralizing data, model distillation compresses a large model into a smaller one, and quantization reduces numeric precision.",
"teach": """**What it is**
Federated learning trains a shared model across many devices (e.g., phones) without their raw data ever leaving the device — only model updates are shared centrally. Model distillation trains a smaller "student" model to mimic a larger "teacher" model's behavior. Quantization reduces the numeric precision of model weights to shrink size and speed up inference.

**Why it matters**
These techniques matter when data privacy prevents centralizing data (federated learning), or when you need a large model's capability in a much smaller, cheaper-to-run package (distillation, quantization).

**How it works**
In federated learning, each device trains locally on its own data, then sends only the resulting model updates (not the raw data) to a central server, which aggregates updates from many devices into an improved shared model. Distillation trains the student model to match the teacher's output probabilities (not just hard labels), transferring more nuanced "knowledge" than labels alone would provide.

**Common mistake**
Assuming federated learning provides perfect privacy guarantees by default — model updates can still leak information about the underlying data without additional privacy techniques like differential privacy.""",
"quiz": """**Q1. What is shared in federated learning, instead of raw data?**  
A) Nothing is shared  B) Model updates/gradients from each device  C) The device's entire dataset  D) User passwords  
**Answer: B**

**Q2. What does model distillation train a smaller model to do?**  
A) Ignore the larger model entirely  B) Mimic a larger "teacher" model's outputs/behavior  C) Only memorize hard labels  D) Replace the need for any training data  
**Answer: B**

**Q3. Does federated learning guarantee complete data privacy by default?**  
A) Yes, always  B) No — model updates can still leak information without added privacy techniques  C) Privacy isn't a consideration in federated learning  D) It guarantees privacy only for images  
**Answer: B**"""
},

"Reading Research Papers": {
"explain": "Building the skill to actually learn from the ML research literature: a systematic reading method, reproducing published results yourself, and writing up clear technical reports of what you learned.",
"teach": """**What it is**
This is a meta-skill: having a systematic approach to reading dense research papers (rather than getting lost line-by-line), reproducing a paper's key results yourself in code, and writing clear technical summaries of what you learned.

**Why it matters**
The field moves fast — the ability to independently read and evaluate a new paper (rather than waiting for a blog post explaining it) is a genuine career differentiator.

**How it works**
A common reading method is multiple passes: first skim the abstract, figures, and conclusion to get the gist; then a full read for understanding; then a close read of the method/math section, checking assumptions and limitations. Reproducing results (even at a smaller scale) forces genuine understanding — a paper often "makes sense" on read-through but reveals hidden assumptions the moment you try to actually implement it. Writing a summary report cements what you learned and creates something you can show as a portfolio artifact.

**Common mistake**
Reading a paper start-to-finish once, linearly, like a novel — dense technical papers are usually better understood through multiple targeted passes than one straight read.""",
"quiz": """**Q1. What is a common effective strategy for reading dense research papers?**  
A) Read once, start to finish, linearly  B) Multiple passes: skim first for gist, then deeper reads for detail and method understanding  C) Only read the abstract  D) Skip the math entirely  
**Answer: B**

**Q2. Why is reproducing a paper's results valuable, even at small scale?**  
A) It isn't valuable  B) It forces genuine understanding and reveals assumptions a read-through alone might miss  C) It's required to publish anything  D) It guarantees identical results always  
**Answer: B**

**Q3. What's a benefit of writing a technical report after reading a paper?**  
A) None  B) It cements understanding and creates a shareable portfolio artifact  C) It replaces the need to understand the paper  D) It's only useful for academics  
**Answer: B**"""
},

"ML System Design": {
"explain": "The interview-critical skill of designing a full ML system on a whiteboard: using a repeatable framework, gathering requirements first, and reasoning explicitly about trade-offs.",
"teach": """**What it is**
ML system design is about architecting a complete ML-powered system (not just a model) — using a consistent framework, starting from requirements gathering (what's the actual goal, constraints, and scale?), and explicitly reasoning through trade-offs (accuracy vs. latency, build vs. buy, batch vs. real-time).

**Why it matters**
This is a standard, heavily-weighted round in ML engineering interviews at most serious companies — and the actual skill of designing systems well is exactly what senior ML engineers are paid for.

**How it works**
A good framework typically moves through: clarify requirements and constraints, define the metric that matters, sketch the overall system (data → training → serving → monitoring), then dive deep into one or two components the interviewer probes further. Explicitly stating trade-offs out loud (e.g., "I'd choose a simpler model here because interpretability matters more than the last 2% of accuracy for this use case") is often more impressive than jumping straight to a complex solution.

**Common mistake**
Diving straight into model architecture details before clarifying requirements, scale, and constraints — this is the single most common mistake in ML system design interviews.""",
"quiz": """**Q1. What should typically come first in an ML system design interview?**  
A) Choosing a specific model architecture  B) Clarifying requirements, constraints, and the metric that matters  C) Writing code  D) Discussing GPU brands  
**Answer: B**

**Q2. Why is explicitly stating trade-offs valuable in these interviews?**  
A) It isn't valuable  B) It demonstrates senior-level judgment, not just technical knowledge  C) It wastes time  D) Interviewers prefer no explanation at all  
**Answer: B**

**Q3. What's the most common mistake candidates make in ML system design interviews?**  
A) Asking too many questions  B) Jumping straight to model details before clarifying requirements and scale  C) Discussing trade-offs  D) Sketching a system diagram  
**Answer: B**"""
},

"Case Studies": {
"explain": "Practicing ML system design on real, common problem types: recommender systems, search ranking, and fraud detection — each with characteristic constraints and design patterns.",
"teach": """**What it is**
Working through canonical ML system design problems — recommender systems (suggesting relevant items to users), search ranking (ordering results by relevance), and fraud detection (flagging suspicious activity) — each has recurring, well-known design patterns worth knowing cold.

**Why it matters**
These three problem types (or close variants) show up constantly in ML system design interviews across the industry — practicing them specifically pays off disproportionately.

**How it works**
Recommender systems typically combine candidate generation (quickly narrowing millions of items to a few hundred plausible ones) with ranking (a more expensive, precise model scoring that shortlist). Search ranking similarly often uses a fast retrieval stage plus a slower reranking stage. Fraud detection usually deals with extreme class imbalance and needs to balance catching fraud (recall) against not annoying legitimate users with false positives (precision), often under strict latency constraints since decisions happen at transaction time.

**Common mistake**
Treating every case study as if it needs the same solution — the "recommend a product" pattern and the "detect fraud in real-time" pattern have meaningfully different constraints (personalization quality vs. low-latency precision) that should shape different designs.""",
"quiz": """**Q1. What are the two typical stages in a large-scale recommender system?**  
A) Training and testing only  B) Candidate generation (narrowing options) followed by ranking (precise scoring)  C) Only ranking, no candidate generation  D) Data cleaning and visualization  
**Answer: B**

**Q2. Why is class imbalance a central concern in fraud detection system design?**  
A) It isn't a concern  B) Fraud is rare relative to legitimate transactions, requiring careful precision/recall balancing  C) Fraud detection doesn't use classification  D) It only matters for images  
**Answer: B**

**Q3. Why do fraud detection systems often have strict latency constraints?**  
A) They don't  B) Decisions often need to happen in real-time at the moment of a transaction  C) Latency doesn't matter for fraud  D) Only batch processing is used for fraud  
**Answer: B**"""
},

"Behavioral & Portfolio Prep": {
"explain": "Preparing to talk about your own work clearly and compellingly: the STAR method for structuring behavioral answers, and project storytelling for presenting your portfolio work.",
"teach": """**What it is**
Behavioral prep uses the STAR method (Situation, Task, Action, Result) to structure clear answers to "tell me about a time..." questions. Project storytelling is about presenting your own portfolio projects (like the ones in this roadmap) in a compelling, structured way.

**Why it matters**
Strong technical skills can still lose an offer if you can't clearly communicate your own decisions, trade-offs, and impact — this is a skill that needs deliberate practice, same as coding.

**How it works**
STAR structures an answer: the Situation (context), the Task (your specific responsibility), the Action (what you actually did — this should be the bulk of the answer), and the Result (the outcome, ideally with a concrete number or clear impact). Project storytelling for a portfolio piece similarly benefits from a clear arc: the problem, your approach and key decisions, the trade-offs you made and why, and the outcome/what you'd improve next.

**Common mistake**
Spending most of a STAR answer describing the Situation and Task in detail, then rushing through the Action (the part that actually shows your skills and decision-making) in one sentence.""",
"quiz": """**Q1. What does the "A" in STAR stand for?**  
A) Analysis  B) Action  C) Assessment  D) Assumption  
**Answer: B**

**Q2. Which part of a STAR answer should typically get the most detail?**  
A) Situation  B) Action — what you specifically did  C) Task  D) None, keep it all equally brief  
**Answer: B**

**Q3. What makes project storytelling for a portfolio piece compelling?**  
A) Listing every library used  B) A clear arc: problem, approach, trade-offs, and outcome  C) Only showing the final result with no context  D) Avoiding mentioning any challenges faced  
**Answer: B**"""
},

"Mock Interviews": {
"explain": "Rehearsing under realistic conditions across the three main ML interview formats: system design, coding, and ML theory — building the fluency that only comes from practice.",
"teach": """**What it is**
Structured practice across the typical ML interview loop: system design mocks (whiteboarding a full ML system), coding mocks (data structures/algorithms, sometimes ML-specific coding), and ML theory mocks (explaining concepts like the ones throughout this roadmap, clearly and correctly under pressure).

**Why it matters**
Knowing material and being able to explain it fluently, live, under mild pressure, in front of another person, are genuinely different skills — mock interviews are what closes that gap.

**How it works**
Effective mock practice includes a real time limit, a partner (or AI) playing interviewer and asking follow-up questions, and — critically — feedback afterward on both technical correctness and communication clarity. Recording yourself (or having a partner note timing/clarity issues) surfaces habits you can't easily notice yourself, like rushing to code before clarifying requirements.

**Common mistake**
Only doing mock interviews solo, silently, in your head — practicing out loud, to another person or even just narrating aloud alone, is what actually builds interview-day fluency.""",
"quiz": """**Q1. Why do mock interviews matter even if you know the material well?**  
A) They don't matter  B) Explaining concepts fluently under pressure, live, is a distinct skill from just knowing them  C) Mocks replace the need to actually study  D) They only test typing speed  
**Answer: B**

**Q2. What's a key part of effective mock interview practice?**  
A) Studying alone in silence only  B) Practicing out loud with real time limits and getting feedback  C) Skipping follow-up questions  D) Avoiding any time pressure  
**Answer: B**

**Q3. What common issue does practicing out loud help surface?**  
A) Nothing useful  B) Habits like rushing to solve before clarifying requirements  C) Your typing speed only  D) Your internet connection quality  
**Answer: B**"""
},

"Resume & LinkedIn": {
"explain": "Presenting your work effectively on paper and online: structuring a resume that highlights impact, quantifying your results, and optimizing your LinkedIn profile for discoverability and credibility.",
"teach": """**What it is**
This covers resume structure (organizing experience/projects for quick scanning), quantifying impact (turning vague duties into measurable results), and LinkedIn optimization (making your profile discoverable and credible to recruiters).

**Why it matters**
A resume gets seconds of attention from a recruiter or hiring manager — poor structure or vague bullet points can bury genuinely strong work.

**How it works**
Strong resume bullets follow a pattern like "did X, measured by Y, resulting in Z" — e.g., "Built a fraud detection GNN, reducing false positives by 30% compared to the existing rule-based system" is far stronger than "worked on fraud detection." LinkedIn optimization means a clear headline (not just a job title), a summary that tells your story, and projects/skills sections that mirror the same measurable language as your resume.

**Common mistake**
Listing responsibilities instead of accomplishments — "responsible for building ML models" says nothing about whether that work actually succeeded or mattered.""",
"quiz": """**Q1. What makes a resume bullet point strong?**  
A) Listing every tool you've ever touched  B) A clear description of what you did plus a measurable result  C) Being as long as possible  D) Using as much jargon as possible  
**Answer: B**

**Q2. What's wrong with a bullet like "responsible for building ML models"?**  
A) Nothing  B) It describes a duty, not an accomplishment or measurable outcome  C) It's too specific  D) It's too short  
**Answer: B**

**Q3. What should a LinkedIn headline ideally communicate?**  
A) Just your job title  B) More than a job title — your focus/story, to stand out and be discoverable  C) Nothing, headlines don't matter  D) Only your years of experience  
**Answer: B**"""
},

"Portfolio Site": {
"explain": "Turning your projects into a public showcase: writing clear project write-ups, polishing your GitHub READMEs, and deploying a personal site to present it all.",
"teach": """**What it is**
Building a portfolio means writing clear project write-ups (the story behind each project, not just code), polishing GitHub READMEs (often the first thing anyone sees of your work), and deploying a personal site tying it all together.

**Why it matters**
A working project with no explanation of the problem, your approach, or your results is far less persuasive to a recruiter or hiring manager than the same project clearly presented.

**How it works**
A good README typically includes: what the project does and why, how to run it, key technical decisions/trade-offs, and results (with numbers or visuals where possible). A personal site aggregates your best 3-5 projects (quality over quantity) with clear write-ups, linking back to the code, plus a short bio and contact info.

**Common mistake**
Uploading dozens of unfinished, unexplained projects instead of a few polished, well-documented ones — quantity without quality actually hurts your portfolio's impression.""",
"quiz": """**Q1. What should a good project README include beyond just the code?**  
A) Nothing else is needed  B) The problem, approach, key decisions, and results  C) Only a list of dependencies  D) Your personal contact information only  
**Answer: B**

**Q2. Is it better to showcase many unfinished projects or a few polished ones?**  
A) Many unfinished projects  B) A few polished, well-documented projects  C) It doesn't matter at all  D) Neither, just link to GitHub with no curation  
**Answer: B**

**Q3. Why does a personal site help beyond just having GitHub repos?**  
A) It doesn't help  B) It curates and presents your best work clearly, rather than making visitors dig through repos  C) GitHub is not allowed for recruiters to see  D) Personal sites replace the need for a resume  
**Answer: B**"""
},

"Technical Interview Prep": {
"explain": "Sharpening the core skills tested in technical rounds: consistent coding practice and reviewing ML theory so you can explain concepts (like everything else in this roadmap) clearly and correctly.",
"teach": """**What it is**
Focused preparation for technical interview rounds: regular coding practice (data structures/algorithms) and reviewing ML theory so you can explain roadmap concepts — like gradient descent, regularization, or attention — clearly and accurately under interview conditions.

**Why it matters**
Technical interviews test both whether you can code, and whether you deeply understand the ML fundamentals you've been building all roadmap — not just whether you can call a library function.

**How it works**
Consistent, spaced coding practice (a bit regularly, not one huge cram session) builds pattern recognition for common problem types. ML theory review benefits from being able to explain a concept simply (as if teaching someone else) — if you can't explain it plainly, you likely don't understand it as deeply as you think.

**Common mistake**
Only practicing problems you already know how to solve — real improvement comes from deliberately practicing problem types you find difficult or unfamiliar.""",
"quiz": """**Q1. Why is spaced, regular coding practice usually better than cramming?**  
A) It isn't better  B) It builds durable pattern recognition rather than short-term memorization  C) Cramming is always more effective  D) Practice frequency doesn't matter  
**Answer: B**

**Q2. What's a good test of whether you truly understand an ML concept?**  
A) Whether you've memorized its name  B) Whether you can explain it simply, as if teaching someone else  C) Whether you've used a library that implements it  D) Whether it appeared in a paper  
**Answer: B**

**Q3. What's a common mistake in coding interview prep?**  
A) Practicing unfamiliar problem types  B) Only practicing problems you're already comfortable with  C) Reviewing solutions afterward  D) Timing yourself  
**Answer: B**"""
},

"System Design Prep": {
"explain": "Getting interview-ready specifically for system design rounds: running realistic mock system design sessions and iterating based on direct feedback.",
"teach": """**What it is**
Targeted preparation for the ML system design interview round specifically — running mock sessions under realistic conditions and, critically, iterating based on feedback rather than just repeating the same mistakes.

**Why it matters**
System design is often the round candidates prepare for least (compared to coding), despite it being heavily weighted at many companies — dedicated prep here is high-leverage.

**How it works**
A mock system design round should mimic real conditions: a time limit, an interviewer (or practice partner) who asks probing follow-up questions, and a whiteboard/doc to sketch on. The valuable part is what happens after — reviewing what went well, what was unclear, and specifically what to do differently next time, then actually doing a different mock to test whether the fix worked.

**Common mistake**
Doing several mock system design sessions in a row without any structured feedback or reflection between them — repetition without feedback mostly just repeats the same gaps.""",
"quiz": """**Q1. Why is system design prep often especially high-leverage?**  
A) It's rarely tested  B) It's heavily weighted at many companies but often under-prepared for  C) It requires no real preparation  D) It's identical to coding prep  
**Answer: B**

**Q2. What makes mock system design practice actually improve performance?**  
A) Just doing many mocks with no feedback  B) Structured feedback and reflection between sessions  C) Avoiding follow-up questions  D) Skipping time limits  
**Answer: B**

**Q3. What should a realistic system design mock include?**  
A) No time limit, no questions  B) A time limit and an interviewer/partner asking probing follow-ups  C) Only a written test with no discussion  D) Pre-shared answers  
**Answer: B**"""
},

"Final Mock Interviews & Outreach": {
"explain": "The final stretch: running full end-to-end mock interview loops, actively networking and reaching out to contacts, and tracking your applications systematically.",
"teach": """**What it is**
The last phase combines full mock loops (simulating an entire interview day: coding, system design, behavioral, back to back), active networking/outreach (reaching out to contacts, including any warm connections you have), and application tracking (systematically managing where you've applied and your status).

**Why it matters**
This is where all the roadmap's preparation gets tested together under realistic conditions, and where a warm introduction (like an existing contact at a target company) can meaningfully change your odds versus a cold application.

**How it works**
A full mock loop back-to-back (not spread across separate days) tests stamina and consistency across formats, closely mimicking a real interview day. Outreach means proactively messaging relevant people — a genuine, specific message referencing their work or your shared context performs far better than a generic "can you refer me" ask. An application tracker (even a simple spreadsheet) prevents you from losing track of where you are in each company's process.

**Common mistake**
Sending the same generic outreach message to everyone — specific, personalized outreach referencing genuine shared context or interest gets meaningfully higher response rates.""",
"quiz": """**Q1. What does a full mock interview loop simulate?**  
A) A single easy question  B) An entire interview day across multiple formats, back to back  C) Only a resume review  D) A single coding problem in isolation  
**Answer: B**

**Q2. Why does personalized outreach outperform generic messages?**  
A) It doesn't  B) It shows genuine interest/context, which gets meaningfully better response rates  C) Generic messages are always better  D) Personalization is illegal on LinkedIn  
**Answer: B**

**Q3. What's the purpose of an application tracker?**  
A) To slow down your search  B) To systematically manage where you've applied and your status in each process  C) It's unnecessary if you apply to only one company  D) To automatically get you interviews  
**Answer: B**"""
},

}
TOPIC_ILLUSTRATIONS = {
"Linear Algebra": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<rect x="15" y="30" width="90" height="90" fill="#fef3b0" stroke="#1e1e1e" stroke-width="2" rx="4"/>
<line x1="45" y1="30" x2="45" y2="120" stroke="#1e1e1e" stroke-width="1"/>
<line x1="75" y1="30" x2="75" y2="120" stroke="#1e1e1e" stroke-width="1"/>
<line x1="15" y1="60" x2="105" y2="60" stroke="#1e1e1e" stroke-width="1"/>
<line x1="15" y1="90" x2="105" y2="90" stroke="#1e1e1e" stroke-width="1"/>
<text x="60" y="145" text-anchor="middle" font-size="11" fill="#555" font-family="Helvetica">Matrix</text>
<path d="M115,75 L150,75" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#a1)"/>
<rect x="160" y="30" width="26" height="90" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" rx="4"/>
<text x="173" y="145" text-anchor="middle" font-size="11" fill="#555" font-family="Helvetica">Vector</text>
<path d="M196,75 L231,75" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#a1)"/>
<rect x="241" y="45" width="26" height="60" fill="#d7f7e0" stroke="#1e9e5a" stroke-width="2" rx="4"/>
<text x="254" y="145" text-anchor="middle" font-size="11" fill="#555" font-family="Helvetica">Result</text>
<defs><marker id="a1" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#3b82f6"/></marker></defs>
</svg>""",

"Calculus": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<path d="M20,25 Q170,155 320,25" fill="none" stroke="#1e1e1e" stroke-width="2.5"/>
<circle cx="65" cy="58" r="8" fill="#3b82f6"/>
<circle cx="120" cy="100" r="8" fill="#7c3aed" opacity="0.75"/>
<circle cx="165" cy="128" r="8" fill="#1e9e5a" opacity="0.75"/>
<text x="170" y="150" text-anchor="middle" font-size="10.5" fill="#555" font-family="Helvetica">Loss decreasing step by step toward the minimum</text>
</svg>""",

"Neural Network Basics": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<g stroke="#c7d2fe" stroke-width="1.5">
<line x1="60" y1="35" x2="170" y2="30"/><line x1="60" y1="35" x2="170" y2="80"/><line x1="60" y1="35" x2="170" y2="130"/>
<line x1="60" y1="80" x2="170" y2="30"/><line x1="60" y1="80" x2="170" y2="80"/><line x1="60" y1="80" x2="170" y2="130"/>
<line x1="60" y1="125" x2="170" y2="30"/><line x1="60" y1="125" x2="170" y2="80"/><line x1="60" y1="125" x2="170" y2="130"/>
<line x1="170" y1="30" x2="270" y2="80"/><line x1="170" y1="80" x2="270" y2="80"/><line x1="170" y1="130" x2="270" y2="80"/>
</g>
<circle cx="60" cy="35" r="11" fill="#fef3b0" stroke="#1e1e1e" stroke-width="2"/>
<circle cx="60" cy="80" r="11" fill="#fef3b0" stroke="#1e1e1e" stroke-width="2"/>
<circle cx="60" cy="125" r="11" fill="#fef3b0" stroke="#1e1e1e" stroke-width="2"/>
<circle cx="170" cy="30" r="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
<circle cx="170" cy="80" r="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
<circle cx="170" cy="130" r="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
<circle cx="270" cy="80" r="13" fill="#d7f7e0" stroke="#1e9e5a" stroke-width="2"/>
<text x="60" y="148" text-anchor="middle" font-size="10" fill="#555" font-family="Helvetica">Input</text>
<text x="170" y="148" text-anchor="middle" font-size="10" fill="#555" font-family="Helvetica">Hidden</text>
<text x="270" y="148" text-anchor="middle" font-size="10" fill="#555" font-family="Helvetica">Output</text>
</svg>""",

"Convolutional Networks": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<g stroke="#ccc" stroke-width="1" fill="#f5f5f5">
<rect x="20" y="20" width="20" height="20"/><rect x="40" y="20" width="20" height="20"/><rect x="60" y="20" width="20" height="20"/><rect x="80" y="20" width="20" height="20"/><rect x="100" y="20" width="20" height="20"/>
<rect x="20" y="40" width="20" height="20"/><rect x="40" y="40" width="20" height="20"/><rect x="60" y="40" width="20" height="20"/><rect x="80" y="40" width="20" height="20"/><rect x="100" y="40" width="20" height="20"/>
<rect x="20" y="60" width="20" height="20"/><rect x="40" y="60" width="20" height="20"/><rect x="60" y="60" width="20" height="20"/><rect x="80" y="60" width="20" height="20"/><rect x="100" y="60" width="20" height="20"/>
<rect x="20" y="80" width="20" height="20"/><rect x="40" y="80" width="20" height="20"/><rect x="60" y="80" width="20" height="20"/><rect x="80" y="80" width="20" height="20"/><rect x="100" y="80" width="20" height="20"/>
<rect x="20" y="100" width="20" height="20"/><rect x="40" y="100" width="20" height="20"/><rect x="60" y="100" width="20" height="20"/><rect x="80" y="100" width="20" height="20"/><rect x="100" y="100" width="20" height="20"/>
</g>
<rect x="40" y="40" width="60" height="60" fill="none" stroke="#3b82f6" stroke-width="3"/>
<text x="70" y="128" text-anchor="middle" font-size="10" fill="#555" font-family="Helvetica">3x3 filter slides across</text>
<path d="M160,70 L200,70" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#a2)"/>
<rect x="210" y="50" width="16" height="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
<rect x="230" y="50" width="16" height="16" fill="#d7f7e0" stroke="#1e9e5a" stroke-width="1.5"/>
<rect x="210" y="70" width="16" height="16" fill="#fdf0d5" stroke="#a67c00" stroke-width="1.5"/>
<rect x="230" y="70" width="16" height="16" fill="#fef3b0" stroke="#1e1e1e" stroke-width="1.5"/>
<text x="228" y="105" text-anchor="middle" font-size="10" fill="#555" font-family="Helvetica">Feature map</text>
<defs><marker id="a2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#3b82f6"/></marker></defs>
</svg>""",

"Transformer Architecture": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<g font-family="Helvetica" font-size="12" fill="#1e1e1e">
<text x="45" y="35">The</text><text x="105" y="35">cat</text><text x="165" y="35">sat</text><text x="220" y="35">on</text><text x="270" y="35">it</text>
</g>
<g stroke="#3b82f6" fill="none">
<path d="M275,40 Q170,90 110,42" stroke-width="2.2" opacity="0.85"/>
<path d="M275,40 Q220,80 50,42" stroke-width="1.4" opacity="0.4"/>
<path d="M275,40 Q250,70 175,42" stroke-width="1.4" opacity="0.4"/>
</g>
<text x="170" y="125" text-anchor="middle" font-size="10.5" fill="#555" font-family="Helvetica">"it" attends most strongly back to "cat"</text>
</svg>""",

"Ensemble Methods": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<g font-family="Helvetica">
<g transform="translate(20,20)"><path d="M15,0 L30,25 L0,25 Z" fill="#fef3b0" stroke="#1e1e1e" stroke-width="1.5"/><rect x="12" y="25" width="6" height="12" fill="#8a5a2b"/></g>
<g transform="translate(75,10)"><path d="M15,0 L30,25 L0,25 Z" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/><rect x="12" y="25" width="6" height="12" fill="#8a5a2b"/></g>
<g transform="translate(20,55)"><path d="M15,0 L30,25 L0,25 Z" fill="#d7f7e0" stroke="#1e9e5a" stroke-width="1.5"/><rect x="12" y="25" width="6" height="12" fill="#8a5a2b"/></g>
<g transform="translate(75,65)"><path d="M15,0 L30,25 L0,25 Z" fill="#fdf0d5" stroke="#a67c00" stroke-width="1.5"/><rect x="12" y="25" width="6" height="12" fill="#8a5a2b"/></g>
</g>
<text x="65" y="140" text-anchor="middle" font-size="10" fill="#555" font-family="Helvetica">Many trees</text>
<path d="M145,75 L185,75" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#a3)"/>
<rect x="195" y="50" width="110" height="50" rx="8" fill="#fff" stroke="#1e1e1e" stroke-width="2"/>
<text x="250" y="80" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e1e1e" font-family="Helvetica">Combined vote</text>
<defs><marker id="a3" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#3b82f6"/></marker></defs>
</svg>""",

"Regression": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<line x1="30" y1="20" x2="30" y2="130" stroke="#999" stroke-width="1.5"/>
<line x1="30" y1="130" x2="310" y2="130" stroke="#999" stroke-width="1.5"/>
<g fill="#3b82f6">
<circle cx="55" cy="105" r="5"/><circle cx="85" cy="95" r="5"/><circle cx="110" cy="100" r="5"/><circle cx="140" cy="75" r="5"/>
<circle cx="170" cy="70" r="5"/><circle cx="200" cy="55" r="5"/><circle cx="230" cy="50" r="5"/><circle cx="260" cy="35" r="5"/><circle cx="285" cy="30" r="5"/>
</g>
<line x1="45" y1="112" x2="295" y2="28" stroke="#1e9e5a" stroke-width="2.5"/>
<text x="170" y="150" text-anchor="middle" font-size="10.5" fill="#555" font-family="Helvetica">Fitting a line to minimize distance to every point</text>
</svg>""",

"Classification": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<g fill="#3b82f6"><circle cx="55" cy="40" r="6"/><circle cx="80" cy="65" r="6"/><circle cx="45" cy="80" r="6"/><circle cx="90" cy="35" r="6"/><circle cx="65" cy="55" r="6"/></g>
<g fill="#e879f9"><circle cx="230" cy="90" r="6"/><circle cx="260" cy="110" r="6"/><circle cx="280" cy="75" r="6"/><circle cx="245" cy="120" r="6"/><circle cx="270" cy="95" r="6"/></g>
<path d="M150,15 L200,140" stroke="#1e1e1e" stroke-width="2.5" stroke-dasharray="6,4"/>
<text x="170" y="152" text-anchor="middle" font-size="10.5" fill="#555" font-family="Helvetica">A decision boundary separating two classes</text>
</svg>""",

"RAG Fundamentals": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<rect x="10" y="55" width="70" height="45" rx="8" fill="#fef3b0" stroke="#1e1e1e" stroke-width="2"/>
<text x="45" y="82" text-anchor="middle" font-size="11" font-family="Helvetica">Query</text>
<path d="M84,77 L114,77" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#a4)"/>
<rect x="122" y="55" width="80" height="45" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
<text x="162" y="76" text-anchor="middle" font-size="11" font-family="Helvetica">Retrieve</text>
<text x="162" y="90" text-anchor="middle" font-size="9" fill="#555" font-family="Helvetica">top chunks</text>
<path d="M206,77 L236,77" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#a4)"/>
<rect x="244" y="55" width="86" height="45" rx="8" fill="#d7f7e0" stroke="#1e9e5a" stroke-width="2"/>
<text x="287" y="76" text-anchor="middle" font-size="11" font-family="Helvetica">Generate</text>
<text x="287" y="90" text-anchor="middle" font-size="9" fill="#555" font-family="Helvetica">grounded answer</text>
<defs><marker id="a4" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#3b82f6"/></marker></defs>
</svg>""",

"Docker Fundamentals": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<rect x="100" y="110" width="140" height="24" fill="#fdf0d5" stroke="#a67c00" stroke-width="1.5"/>
<text x="170" y="126" text-anchor="middle" font-size="10" font-family="Helvetica">Base OS layer</text>
<rect x="100" y="86" width="140" height="24" fill="#fef3b0" stroke="#1e1e1e" stroke-width="1.5"/>
<text x="170" y="102" text-anchor="middle" font-size="10" font-family="Helvetica">Dependencies layer</text>
<rect x="100" y="62" width="140" height="24" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
<text x="170" y="78" text-anchor="middle" font-size="10" font-family="Helvetica">Your app code</text>
<rect x="85" y="30" width="170" height="28" rx="6" fill="#d7f7e0" stroke="#1e9e5a" stroke-width="2.5"/>
<text x="170" y="49" text-anchor="middle" font-size="11" font-weight="bold" font-family="Helvetica">Running Container</text>
<text x="170" y="150" text-anchor="middle" font-size="10" fill="#555" font-family="Helvetica">One image, runs identically anywhere</text>
</svg>""",

"CI Fundamentals": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<g font-family="Helvetica" font-size="11">
<rect x="10" y="55" width="65" height="42" rx="7" fill="#fef3b0" stroke="#1e1e1e" stroke-width="2"/><text x="42" y="80" text-anchor="middle">Push</text>
<path d="M79,76 L104,76" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#a5)"/>
<rect x="112" y="55" width="65" height="42" rx="7" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/><text x="144" y="80" text-anchor="middle">Test</text>
<path d="M181,76 L206,76" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#a5)"/>
<rect x="214" y="55" width="65" height="42" rx="7" fill="#d7f7e0" stroke="#1e9e5a" stroke-width="2"/><text x="246" y="80" text-anchor="middle">Deploy</text>
<text x="246" y="45" text-anchor="middle" font-size="16" fill="#1e9e5a">&#10003;</text>
</g>
<text x="170" y="130" text-anchor="middle" font-size="10" fill="#555" font-family="Helvetica">Every push is automatically checked before it can ship</text>
</svg>""",

"Agents": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<circle cx="90" cy="55" r="34" fill="#fef3b0" stroke="#1e1e1e" stroke-width="2"/><text x="90" y="59" text-anchor="middle" font-size="11" font-family="Helvetica">Reason</text>
<circle cx="250" cy="55" r="34" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/><text x="250" y="59" text-anchor="middle" font-size="11" font-family="Helvetica">Act</text>
<circle cx="170" cy="125" r="34" fill="#d7f7e0" stroke="#1e9e5a" stroke-width="2"/><text x="170" y="129" text-anchor="middle" font-size="11" font-family="Helvetica">Observe</text>
<path d="M122,45 Q170,20 218,45" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#a6)"/>
<path d="M235,85 Q210,105 195,105" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#a6)"/>
<path d="M148,105 Q125,95 108,85" stroke="#3b82f6" stroke-width="2" fill="none" marker-end="url(#a6)"/>
<defs><marker id="a6" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#3b82f6"/></marker></defs>
</svg>""",

"Data Drift": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<line x1="20" y1="130" x2="320" y2="130" stroke="#999" stroke-width="1.5"/>
<path d="M40,130 Q100,20 160,130" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<path d="M140,130 Q200,45 260,130" fill="none" stroke="#e879f9" stroke-width="2.5" stroke-dasharray="5,4"/>
<text x="100" y="145" text-anchor="middle" font-size="10" fill="#3b82f6" font-family="Helvetica">Training data</text>
<text x="235" y="145" text-anchor="middle" font-size="10" fill="#c026d3" font-family="Helvetica">Live data (shifted)</text>
</svg>""",

"Embeddings & Vector Search": """<svg viewBox="0 0 340 160" width="340" height="160" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
<rect width="340" height="160" fill="#fdfdfb"/>
<g fill="#c7d2fe"><circle cx="60" cy="40" r="5"/><circle cx="270" cy="120" r="5"/><circle cx="230" cy="30" r="5"/><circle cx="90" cy="130" r="5"/></g>
<circle cx="150" cy="80" r="7" fill="#3b82f6"/>
<circle cx="170" cy="65" r="6" fill="#7c3aed"/>
<circle cx="180" cy="95" r="6" fill="#7c3aed"/>
<circle cx="140" cy="105" r="6" fill="#7c3aed"/>
<circle cx="165" cy="82" r="45" fill="none" stroke="#1e9e5a" stroke-width="2" stroke-dasharray="5,4"/>
<text x="165" y="145" text-anchor="middle" font-size="10.5" fill="#555" font-family="Helvetica">Nearest neighbors in vector space = most similar meaning</text>
</svg>""",

}
