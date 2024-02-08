from flask import Flask, request
app = Flask(__name__)
def filter_df(input_df, company, difficulty, rating):
@app.route('/')
def handle_query():
    query_params = request.args
    company = query_params.get('company')
    difficulty = query_params.get('difficulty')
    rating = float(query_params.get('rating'))

    file_path = os.path.join(os.path.dirname(__file__), 'excelfile.csv')
    file = pd.read_csv(file_path)

    filtered_data = filter_df(file, company, difficulty, rating)
    courses_list = filtered_data.to_dict(orient='records')

    return {"filtered_data": courses_list}

if __name__ == '__main__':
    app.run(debug=True) 
