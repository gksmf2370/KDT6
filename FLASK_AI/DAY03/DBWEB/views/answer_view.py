from datetime import datetime

from flask import Blueprint, url_for, request
from werkzeug.utils import redirect

from DBWEB import DB
from DBWEB.models.models import Question, Answer

# Blueprint 인스턴스 생성
answerBP = Blueprint( 'answer', import_name=__name__, url_prefix='/answer')

@answerBP.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']

    answer = Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer)
    DB.session.commit()
    return redirect(url_for('MAIN.questionItem', qid=question_id))
