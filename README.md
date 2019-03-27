# SoftwareEngineering-FirstDemo

KA$H stands for the Knowledgeable Automated Stock Handler. In essence, it is a stock handling system that allows users to get information regarding the sentiment and statistical trends of various stocks and have KA$H trade the stocks for them based on prediction data based on sentiment and statistical trends. To meet this lofty goal, the system is split into three sub-projects that go into greater detail regarding the individual features that must be met. The sub-projects are the Sentiment Analyzer, Technical Forecaster, and the Auto-Trader.

Sentiment Analyzer:
	The Sentiment Analyzer is responsible for aggregating news data from the Internet regarding a particular stock that is currently being traded in the New York Stock Exchange and then analyzing that data to determine a sentiment value. In the current release of KA$H, the user will be able to get an intimate understanding of the Sentiment Analyzer’s backend. The user will be able to enter any stock ticker exactly as it appears in the NYSE and have their input properly error-checked to ensure that they actually did type an entry that it is in the NYSE. If so, they will receive an averaged score between -1.0 and 1.0, where -1 represents extreme negative sentiment and 1 represents extreme positive sentiment. In addition, the Analyzer will return the top five headlines that it retrieved when using the News API to gather different sources. Lastly, the Sentiment Analyzer will map the prediction score that it calculated to a prediction of future stock price trend. A more positive score will result in a prediction for an increase in stock price, while the opposite will trigger a prediction for a decrease in stock price. Roughly neutral sentiment maps to constant stock prices. Lastly, the SentimentAnalyzer updates the database with its newly calculated sentiment every time it is fired, which is beneficial for the Auto-Trader to have a ready supply of fresh data whenever they choose to interact with our API. 
	Installation: In order to install the SA successfully, the user must have the following packages installed on their computer.
Python 3.6, which can be downloaded from python.org
An IDE for running Python, ideally PyCharm. PyCharm should be configured to a Python 3.6 interpreter
To choose the Python 3.6 Interpreter, navigate to Preferences->Project Interpreter and choose the Python 3.6 you have installed on your system.

Within PyCharm, navigate to Preferences->Project Interpreter and click on the + sign
From there, search and install pip and set it to its newest version.
Then add Pillow using the same procedure as used for pip
Repeat for requests, mysql-connector-python, and nltk
After installing all those packages, the code should have no errors in Pycharm. If there are errors, try to repeat the above steps and make sure that you are installing the components to the correct directory within Pycharm so it takes effect.
To run the code, navigate to SentimentDemo/SentimentController.py and right-click the file to run it. 
As of this edition, this will allow the tKinter-based GUI to fire up in a separate window and allow the user to search a stock and receive its sentiment and prediction in real-time while also updating the AWS-hosted database.

Technical Forecaster:
	The Technical Forecaster is responsible for using mathematical models to generate a prediction about the future price of a particular stock that is listed on the New York Stock Exchange. In the current release of KA$H the use will be able to view the results of various calculations that will be aggregated into a final prediction in the future. The user will enter a stock ticker that matches exactly with a stock on the NYSE (an error will be sent if the stock name does not match). The user will then be shown the results of several calculations. The first result will be for Rate of Change: an unbounded number that may be positive or negative that indicates the price has been increasing recently if it is positive and indicates that the price has been decreasing recently if it is negative whose magnitude indicates how quickly it is increasing or decreasing. The second result will be for the Stochastic Oscillator: a number between 0 and 100 that indicates the momentum of a stock, with numbers above 50 indicating strong momentum and numbers below 50 indicating weak momentum. The third result will be for the Accumulative Swing Index, a number between -100 and 100 that indicates the long term likelihood of a stock to increase or decrease in price, with a negative number indicating a likelihood to decrease and a positive number indicating a likelihood to increase. The magnitude of the number indicates the degree of increase or decrease. The fourth result will be for the ARIMA model, which uses past stock data and an AutoRegressive Integrated Moving Average to fit the stock data to a curve in order to get a prediction about the future price. The ARIMA prediction will be an actual stock price, not an index value. These results will be aggregated into a total prediction, which will be displayed below the current stock price. All of these calculation results will be color coded when displayed to the user, with green indicating that it is likely the future stock price will be higher and red indicating that it will be lower. 
	Installation: In order to use this release of the Technical Forecaster, the user must have the following files installed on their computer:
Python 3.6 or newer, which can be downloaded from python.org
An IDE for running Python (we used PyCharm and will configure the rest of the instructions as though you are also using PyCharm). PyCharm should be configured to a Python 3.6 interpreter
To choose the Python 3.6 Interpreter, navigate to Preferences->Project Interpreter and choose the Python 3.6 you have installed on your system.
Several Python Modules are required, which can be downloaded within PyCharm by navigating to Preferences->Project Interpreter and click on the + sign
From there, search and install pip and set it to its newest version.
Then add Pillow using the same procedure as used for pip
Repeat for mysql-connector-python, statsmodels, and scipy
After installing all those packages, the code should have no errors in Pycharm. If there are errors, try to repeat the above steps and make sure that you are installing the components to the correct directory within Pycharm so it takes effect.
To run the code, navigate to techController.py and right-click the file to run it. (You do not need to run any other file).
As of this edition, this will allow the tKinter-based GUI to fire up in a separate window and allow the user to search a stock and receive its prediction and calculations for other indices.

Auto-Trader:
The Autotrader makes purchases for the user as hold, sell, buy. It collects sentiment from sentiment analyzer and fetches the predictions and price movements from forecaster. These are fed to the neural network, whose output is used to make one of the following decisions: Sell, Buy, Hold. The AutoTrader runs in sessions, where the user gets to adjust the period of trading according to preference. It also receives the stock ticker the user is interested in and limits trading decisions to this stock. After trading sessions end, transactions made are logged and sent as a report to the user.
Installation: To run AutoTrader, the user must have the following files installed on their computer:
•Python 3.6 or newer, which can be downloaded from python.org
• An IDE for running Python (we used PyCharm and will configure the rest of the instructions as though you are also using PyCharm). PyCharm should be configured to a Python 3.6 interpreter
To choose the Python 3.6 Interpreter, navigate to Preferences->Project Interpreter and choose the Python 3.6 you have installed on your system.
Several Python Modules are required, which can be downloaded within PyCharm by navigating to Preferences->Project Interpreter and click on the + sign
From there, search and install pip and set it to its newest version.
Then add Pillow using the same procedure as used for pip.
Repeat for mysql-connector-python,  Alpha_vantage.timeseries and Numpy.
After installing all those packages, the code should have no errors in Pycharm. If there are errors, try to repeat the above steps and make sure that you are installing the components to the correct directory within Pycharm so it takes effect.
To run the code, navigate to techController.py and right-click the file to run it. (You do not need to run any other file).
 

