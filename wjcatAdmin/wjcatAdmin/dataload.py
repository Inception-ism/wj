import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wjcatAdmin.settings")
django.setup()

from myAdmin.models import Question, Options  # 替换为你的实际模型和应用名称

# 假定每个问题的默认选项
DEFAULT_OPTIONS = ['1', '2', '3', '4', '5']

def load_questions_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def create_questions_with_options(questions, wjId):
    for question_title in questions:
        # 创建新问题
        question = Question.objects.create(
            title=question_title, 
            type='radio',  # 假设每个问题是单选
            wjId=wjId,     # 使用提供的问卷 ID
            must=True      # 假设每个问题都是必答
        )

        # 为每个问题创建默认选项
        for option_title in DEFAULT_OPTIONS:
            Options.objects.create(
                questionId=question.id,
                title=option_title
            )
        print(f"Created question '{question_title}' with default options.")

file_path = 'wjcatAdmin\data.txt'  # 替换为你的文本文件路径
wjId = 2 # 替换为关联的问卷 ID
questions = load_questions_from_txt(file_path)
create_questions_with_options(questions, wjId)