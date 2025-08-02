from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import io
import os

app = Flask(__name__)

def load_books():
    df = pd.read_csv('trius_book_list.csv')
    # Replace NaN values with '-'
    df = df.fillna('-')
    return df

@app.route('/')
def index():
    books = load_books()
    sort_by = request.args.get('sort', '번호')
    order = request.args.get('order', 'asc')
    
    if sort_by in books.columns:
        books = books.sort_values(by=sort_by, ascending=(order == 'asc'))
    
    return render_template('index.html', books=books.to_dict('records'))

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    books = load_books()
    sort_by = request.args.get('sort', '번호')
    order = request.args.get('order', 'asc')
    
    if query:
        filtered_books = books[
            books['도서명'].str.lower().str.contains(query) |
            books['저자'].str.lower().str.contains(query)
        ]
    else:
        filtered_books = books
    
    if sort_by in books.columns:
        filtered_books = filtered_books.sort_values(by=sort_by, ascending=(order == 'asc'))
        
    return render_template('index.html', books=filtered_books.to_dict('records'))

@app.route('/download')
def download():
    books = load_books()
    
    # Create CSV in memory
    output = io.StringIO()
    books.to_csv(output, index=False, encoding='utf-8-sig')
    output.seek(0)
    
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8-sig')),
        mimetype='text/csv',
        as_attachment=True,
        download_name='trius_book_list.csv'
    )

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': '파일이 없습니다.'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': '선택된 파일이 없습니다.'})
    
    if not file.filename.endswith('.csv'):
        return jsonify({'success': False, 'message': 'CSV 파일만 업로드 가능합니다.'})
    
    try:
        # 임시 파일로 저장
        temp_path = 'temp_book_list.csv'
        file.save(temp_path)
        
        # CSV 파일 검증
        df = pd.read_csv(temp_path)
        required_columns = ['번호', '도서명', '저자', '분류', '추천 대상']
        if not all(col in df.columns for col in required_columns):
            os.remove(temp_path)
            return jsonify({'success': False, 'message': '필수 열이 누락되었습니다.'})
        
        # 기존 파일 백업
        if os.path.exists('trius_book_list.csv'):
            os.rename('trius_book_list.csv', 'trius_book_list.csv.bak')
        
        # 새 파일 적용
        os.rename(temp_path, 'trius_book_list.csv')
        
        return jsonify({'success': True, 'message': '도서목록이 업데이트되었습니다.'})
    except Exception as e:
        # 오류 발생 시 백업 파일 복구
        if os.path.exists('trius_book_list.csv.bak'):
            os.rename('trius_book_list.csv.bak', 'trius_book_list.csv')
        return jsonify({'success': False, 'message': f'파일 처리 중 오류가 발생했습니다: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) 