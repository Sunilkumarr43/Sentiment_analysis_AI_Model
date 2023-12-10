from flask import Flask, request, jsonify
from sentiment_analysis_model import analyze_sentiment
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Assuming you have a MySQL database running locally
DATABASE_URL = "mysql://username:password@localhost:3306/your_database"
engine = create_engine(DATABASE_URL, echo=True)

# Define a SQLAlchemy model for the sentiment results
Base = declarative_base()

class SentimentResult(Base):
    __tablename__ = 'sentiment_results'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_endpoint():
    data = request.get_json()
    text = data['text']
    sentiment = analyze_sentiment(text)

    # Store results in MySQL database
    with Session() as session:
        result = SentimentResult(text=text, sentiment=sentiment)
        session.add(result)
        session.commit()

    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
