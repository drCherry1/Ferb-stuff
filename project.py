
import streamlit as st
import random 
import pandas as pd
from datetime import date


# ==========================================
# PAGE SETTINGS
# ==========================================
st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="centered"
)


# ==========================================
# SESSION STATE
# ==========================================

if "calculator" not in st.session_state:
    st.session_state.calculator = ""

if "gpa" not in st.session_state:
    st.session_state.gpa = None

if "quiz_percentage" not in st.session_state:
    st.session_state.quiz_percentage = None

if "subjects" not in st.session_state:
    st.session_state.subjects = [
        "Mathematics",
        "English",
        "Science"
    ]

if "grade_results" not in st.session_state:
    st.session_state.grade_results = None

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = [
        {
            "question": "",
            "A": "",
            "B": "",
            "C": "",
            "D": "",
            "correct": "A"
        }
        for _ in range(5)
    ]

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_current" not in st.session_state:
    st.session_state.quiz_current = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False


# ==========================================
# WELCOME
# ==========================================

st.title("🎓 Student Dashboard")

st.header("👋 Welcome back!")

st.write(
    "Your personal place for studying, "
    "calculating, checking grades, and making quizzes."
)


# ==========================================
# QUICK STATS
# ==========================================

st.markdown("---")
st.subheader("📊 Quick Stats")

if st.session_state.gpa is None:
    gpa_text = "—"
else:
    gpa_text = f"{st.session_state.gpa:.2f}"

if st.session_state.quiz_percentage is None:
    quiz_text = "—"
else:
    quiz_text = f"{st.session_state.quiz_percentage:.1f}%"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎓 GPA", gpa_text)

with col2:
    st.metric("🧠 Quiz", quiz_text)

with col3:
    st.metric("🔥 Streak", "—")


# ==========================================
# MY FIRST PROFILE
# ==========================================

st.markdown("---")
st.title("👤 My First Profile")

st.write(
    "Fill in your information and create your personalized profile!"
)

name = st.text_input("🧑 Name")

age = st.number_input(
    "🎂 Age",
    min_value=1,
    max_value=100,
    step=1
)

school = st.text_input("🏫 School")
subject = st.text_input("📚 Favorite subject")
hobby = st.text_input("🎨 Favorite hobby")

if st.button("✨ Create My Profile"):

    if name and school and subject and hobby:

        st.success("Your profile is ready!")

        st.markdown("---")

        st.header(
            f"Hello! My name is {name}."
        )

        st.write(
            f"🎂 I am **{age} years old**."
        )

        st.write(
            f"🏫 I go to **{school}**."
        )

        st.write(
            f"📚 My favorite subject is **{subject}**."
        )

        st.write(
            f"🎨 I enjoy **{hobby}**."
        )

        st.balloons()

    else:

        st.warning(
            "Please fill in all the fields first!"
        )


# ==========================================
# CALCULATOR
# ==========================================

st.markdown("---")
st.title("🧮 Simple Calculator")


def add_to_calculator(value):
    st.session_state.calculator += value


def clear_calculator():
    st.session_state.calculator = ""


def calculate():
    try:
        result = eval(st.session_state.calculator)
        st.session_state.calculator = str(result)

    except:
        st.session_state.calculator = "Error"


st.text_input(
    "Display",
    key="calculator",
    disabled=True
)


# Row 1
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "7",
        on_click=add_to_calculator,
        args=("7",),
        use_container_width=True
    )

with col2:
    st.button(
        "8",
        on_click=add_to_calculator,
        args=("8",),
        use_container_width=True
    )

with col3:
    st.button(
        "9",
        on_click=add_to_calculator,
        args=("9",),
        use_container_width=True
    )

with col4:
    st.button(
        "÷",
        on_click=add_to_calculator,
        args=("/",),
        use_container_width=True
    )


# Row 2
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "4",
        on_click=add_to_calculator,
        args=("4",),
        use_container_width=True
    )

with col2:
    st.button(
        "5",
        on_click=add_to_calculator,
        args=("5",),
        use_container_width=True
    )

with col3:
    st.button(
        "6",
        on_click=add_to_calculator,
        args=("6",),
        use_container_width=True
    )

with col4:
    st.button(
        "×",
        on_click=add_to_calculator,
        args=("*",),
        use_container_width=True
    )


# Row 3
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "1",
        on_click=add_to_calculator,
        args=("1",),
        use_container_width=True
    )

with col2:
    st.button(
        "2",
        on_click=add_to_calculator,
        args=("2",),
        use_container_width=True
    )

with col3:
    st.button(
        "3",
        on_click=add_to_calculator,
        args=("3",),
        use_container_width=True
    )

with col4:
    st.button(
        "-",
        on_click=add_to_calculator,
        args=("-",),
        use_container_width=True
    )


# Row 4
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "0",
        on_click=add_to_calculator,
        args=("0",),
        use_container_width=True
    )

with col2:
    st.button(
        ".",
        on_click=add_to_calculator,
        args=(".",),
        use_container_width=True
    )

with col3:
    st.button(
        "C",
        on_click=clear_calculator,
        use_container_width=True
    )

with col4:
    st.button(
        "+",
        on_click=add_to_calculator,
        args=("+",),
        use_container_width=True
    )


# Equals
st.button(
    "=",
    on_click=calculate,
    use_container_width=True
)


# ==========================================
# GRADE CALCULATOR
# ==========================================

st.markdown("---")
st.title("🎓 Grade Calculator")

st.write(
    "Enter your marks to calculate your grades, percentage, and GPA."
)


def get_grade(percentage):

    if percentage >= 90:
        return "A+", 4.00

    elif percentage >= 80:
        return "A", 4.00

    elif percentage >= 70:
        return "B", 3.00

    elif percentage >= 60:
        return "C", 2.00

    elif percentage >= 50:
        return "D", 1.00

    else:
        return "F", 0.00


# ==========================================
# SUBJECT FUNCTIONS
# ==========================================

def add_subject():

    number = len(st.session_state.subjects) + 1

    st.session_state.subjects.append(
        f"Subject {number}"
    )


def reset_grades():

    st.session_state.subjects = [
        "Mathematics",
        "English",
        "Science"
    ]

    st.session_state.grade_results = None
    st.session_state.gpa = None

    for key in list(st.session_state.keys()):

        if key.startswith("marks_"):
            del st.session_state[key]


def calculate_grades():

    results = []

    total_marks = 0
    total_maximum = 0
    total_gpa = 0

    for i, subject in enumerate(
        st.session_state.subjects
    ):

        marks = st.session_state.get(
            f"marks_{i}",
            0
        )

        maximum = 100

        percentage = (
            marks / maximum
        ) * 100

        grade, gpa = get_grade(
            percentage
        )

        results.append({

            "name": subject,

            "marks": marks,

            "percentage": percentage,

            "grade": grade,

            "gpa": gpa

        })

        total_marks += marks
        total_maximum += maximum
        total_gpa += gpa


    overall_percentage = (
        total_marks / total_maximum
    ) * 100


    overall_grade, _ = get_grade(
        overall_percentage
    )


    overall_gpa = (
        total_gpa /
        len(st.session_state.subjects)
    )


    st.session_state.grade_results = {

        "subjects": results,

        "total_marks": total_marks,

        "total_maximum": total_maximum,

        "overall_percentage":
            overall_percentage,

        "overall_grade":
            overall_grade,

        "overall_gpa":
            overall_gpa

    }


    # THIS UPDATES THE DASHBOARD GPA

    st.session_state.gpa = overall_gpa


# ==========================================
# SUBJECTS
# ==========================================

st.header("📚 Subjects")

for i, subject in enumerate(
    st.session_state.subjects
):

    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(
            f"### 📖 {subject}"
        )

    with col2:

        st.number_input(
            "Marks",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            key=f"marks_{i}",
            label_visibility="collapsed"
        )


# ==========================================
# GRADE BUTTONS
# ==========================================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:

    st.button(
        "➕ Add Subject",
        on_click=add_subject,
        use_container_width=True
    )

with col2:

    st.button(
        "🔄 Reset",
        on_click=reset_grades,
        use_container_width=True
    )

with col3:

    st.button(
        "🧮 Calculate My Grade",
        on_click=calculate_grades,
        use_container_width=True
    )


# ==========================================
# GRADE RESULTS
# ==========================================

if st.session_state.grade_results is not None:

    results = st.session_state.grade_results

    st.markdown("---")

    st.header("🏆 Overall Performance")

    for result in results["subjects"]:

        st.write(
            f"**📖 {result['name']}** — "
            f"{result['marks']:.0f}/100 — "
            f"{result['percentage']:.1f}% — "
            f"Grade **{result['grade']}** — "
            f"GPA **{result['gpa']:.2f}**"
        )


    st.markdown("---")

    st.header("📊 Final Results")

    st.write(
        f"📝 **Total Marks: "
        f"{results['total_marks']:.0f} / "
        f"{results['total_maximum']:.0f}**"
    )

    st.write(
        f"📈 **Overall Percentage: "
        f"{results['overall_percentage']:.1f}%**"
    )

    st.write(
        f"🏆 **Overall Grade: "
        f"{results['overall_grade']}**"
    )

    st.write(
        f"🎓 **Overall GPA: "
        f"{results['overall_gpa']:.2f}**"
    )


    st.markdown("---")


    if results["overall_grade"] in ["A+", "A"]:

        st.success(
            "🎉 Congratulations on your success! "
            "Excellent work! Keep up the amazing effort! 🌟"
        )

    elif results["overall_grade"] == "B":

        st.info(
            "👏 Great job! You did really well. "
            "Keep working hard and aim even higher! 💪"
        )

    elif results["overall_grade"] == "C":

        st.info(
            "👍 Good effort! You have a solid start. "
            "Keep practicing and you can improve even more! 📚"
        )

    elif results["overall_grade"] == "D":

        st.warning(
            "💪 Keep going! Don't give up. "
            "With more practice and effort, you can improve your results! 🌱"
        )

    else:

        st.error(
            "🌟 Don't be discouraged! Every result is a chance to learn. "
            "Keep studying, practice regularly, and try again! 💪📚"
        )


# ==========================================
# QUIZ MASTER
# ==========================================

st.markdown("---")
st.title("🧠 Quiz Master")

st.write(
    "Create your own multiple-choice quiz!"
)


# ==========================================
# QUIZ FUNCTIONS
# ==========================================

def add_quiz_question():

    st.session_state.quiz_questions.append({

        "question": "",

        "A": "",

        "B": "",

        "C": "",

        "D": "",

        "correct": "A"

    })


def remove_quiz_question():

    if len(
        st.session_state.quiz_questions
    ) > 1:

        st.session_state.quiz_questions.pop()

    else:

        st.warning(
            "You must have at least 1 question."
        )


def start_quiz():

    st.session_state.quiz_started = True

    st.session_state.quiz_current = 0

    st.session_state.quiz_score = 0

    st.session_state.quiz_finished = False

    st.session_state.quiz_percentage = None


def next_question():

    current = st.session_state.quiz_current

    selected = st.session_state.get(
        f"quiz_answer_{current}"
    )

    correct = (
        st.session_state.quiz_questions[
            current
        ]["correct"]
    )

    if selected == correct:

        st.session_state.quiz_score += 1


    # More questions remain

    if current < len(
        st.session_state.quiz_questions
    ) - 1:

        st.session_state.quiz_current += 1

    # Last question

    else:

        # Calculate score INCLUDING final answer

        final_score = st.session_state.quiz_score

        total = len(
            st.session_state.quiz_questions
        )

        st.session_state.quiz_percentage = (
            final_score / total
        ) * 100

        st.session_state.quiz_finished = True


# ==========================================
# QUIZ CREATOR
# ==========================================

if not st.session_state.quiz_started:

    st.subheader("📝 Create Your Questions")


    col1, col2, col3 = st.columns(
        [1, 2, 1]
    )


    with col1:

        st.button(
            "➖",
            on_click=remove_quiz_question,
            use_container_width=True
        )


    with col2:

        st.markdown(
            f"""
            <h3 style="text-align:center;">
            {len(st.session_state.quiz_questions)}
            Questions
            </h3>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.button(
            "➕",
            on_click=add_quiz_question,
            use_container_width=True
        )


    st.markdown("---")


    for i, quiz in enumerate(
        st.session_state.quiz_questions
    ):

        st.subheader(
            f"Question {i + 1}"
        )


        quiz["question"] = st.text_area(
            "Question",
            value=quiz["question"],
            key=f"quiz_question_{i}",
            placeholder="Type your question here..."
        )


        col1, col2 = st.columns(2)


        with col1:

            quiz["A"] = st.text_input(
                "A",
                value=quiz["A"],
                key=f"quiz_A_{i}",
                placeholder="Choice A"
            )


            quiz["C"] = st.text_input(
                "C",
                value=quiz["C"],
                key=f"quiz_C_{i}",
                placeholder="Choice C"
            )


        with col2:

            quiz["B"] = st.text_input(
                "B",
                value=quiz["B"],
                key=f"quiz_B_{i}",
                placeholder="Choice B"
            )


            quiz["D"] = st.text_input(
                "D",
                value=quiz["D"],
                key=f"quiz_D_{i}",
                placeholder="Choice D"
            )


        quiz["correct"] = st.selectbox(
            "✅ Correct Answer",
            ["A", "B", "C", "D"],
            index=[
                "A",
                "B",
                "C",
                "D"
            ].index(
                quiz["correct"]
            ),
            key=f"quiz_correct_{i}"
        )


        st.markdown("---")


    if st.button(
        "🚀 Start Quiz",
        use_container_width=True
    ):

        all_filled = True

        for quiz in st.session_state.quiz_questions:

            if (
                not quiz["question"].strip()
                or not quiz["A"].strip()
                or not quiz["B"].strip()
                or not quiz["C"].strip()
                or not quiz["D"].strip()
            ):

                all_filled = False

                break


        if all_filled:

            start_quiz()

            st.rerun()

        else:

            st.warning(
                "⚠️ Please fill in every question "
                "and all four choices before starting."
            )


# ==========================================
# QUIZ MODE
# ==========================================

else:

    if not st.session_state.quiz_finished:

        current = (
            st.session_state.quiz_current
        )

        quiz = (
            st.session_state.quiz_questions[
                current
            ]
        )


        st.subheader(
            f"Question {current + 1} "
            f"of "
            f"{len(st.session_state.quiz_questions)}"
        )


        st.write(
            f"### {quiz['question']}"
        )


        st.radio(
            "Choose your answer:",
            [
                f"A. {quiz['A']}",
                f"B. {quiz['B']}",
                f"C. {quiz['C']}",
                f"D. {quiz['D']}"
            ],
            key=f"quiz_answer_display_{current}"
        )


        answer_map = {

            f"A. {quiz['A']}": "A",

            f"B. {quiz['B']}": "B",

            f"C. {quiz['C']}": "C",

            f"D. {quiz['D']}": "D"

        }


        selected_display = st.session_state.get(
            f"quiz_answer_display_{current}"
        )


        if selected_display:

            st.session_state[
                f"quiz_answer_{current}"
            ] = answer_map[selected_display]


        st.markdown("---")


        if current < len(
            st.session_state.quiz_questions
        ) - 1:

            st.button(
                "➡️ Next Question",
                on_click=next_question,
                use_container_width=True
            )

        else:

            st.button(
                "🏁 Finish Quiz",
                on_click=next_question,
                use_container_width=True
            )


    # ======================================
    # QUIZ RESULTS
    # ======================================

    else:

        total = len(
            st.session_state.quiz_questions
        )

        score = (
            st.session_state.quiz_score
        )

        percentage = (
            st.session_state.quiz_percentage
        )


        st.balloons()

        st.success(
            "🎉 Quiz Complete!"
        )

        st.header(
            "🏆 Your Results"
        )

        st.write(
            f"### Score: **{score} / {total}**"
        )

        st.write(
            f"### Percentage: **{percentage:.1f}%**"
        )


        if percentage >= 90:

            st.success(
                "🌟 Excellent! You absolutely crushed it!"
            )

        elif percentage >= 80:

            st.success(
                "👏 Great job! You did really well!"
            )

        elif percentage >= 70:

            st.info(
                "👍 Good work! Keep practicing!"
            )

        elif percentage >= 50:

            st.warning(
                "💪 Not bad! Keep studying and try again!"
            )

        else:

            st.error(
                "📚 Keep practicing! You can improve!"
            )


        st.markdown("---")


        if st.button(
            "🔄 Create Another Quiz",
            use_container_width=True
        ):

            st.session_state.quiz_questions = [

                {
                    "question": "",
                    "A": "",
                    "B": "",
                    "C": "",
                    "D": "",
                    "correct": "A"
                }

                for _ in range(5)
            ]

            st.session_state.quiz_started = False

            st.session_state.quiz_current = 0

            st.session_state.quiz_score = 0

            st.session_state.quiz_finished = False

            st.session_state.quiz_percentage = None

            st.rerun()

# ==========================================
# GUESS THE NUMBER GAME
# ==========================================

st.markdown("---")
st.title("🎯 Guess the Number")

st.write(
    "Choose a difficulty, decide how many guesses "
    "you want, and try to find the secret number!"
)

# GAME SESSION STATE

if "number_game_difficulty" not in st.session_state:
    st.session_state.number_game_difficulty = "Normal"

if "number_game_active" not in st.session_state:
    st.session_state.number_game_active = False

if "number_game_secret" not in st.session_state:
    st.session_state.number_game_secret = None

if "number_game_max_guesses" not in st.session_state:
    st.session_state.number_game_max_guesses = 5

if "number_game_guesses_used" not in st.session_state:
    st.session_state.number_game_guesses_used = 0

if "number_game_won" not in st.session_state:
    st.session_state.number_game_won = None

if "number_game_message" not in st.session_state:
    st.session_state.number_game_message = ""


# DIFFICULTY SETTINGS

difficulty_settings = {
    "Normal": {
        "minimum": 1,
        "maximum": 50,
        "icon": "🟢"
    },
    "Intermediate": {
        "minimum": 1,
        "maximum": 150,
        "icon": "🔵"
    },
    "Advanced": {
        "minimum": 0,
        "maximum": 700,
        "icon": "🟠"
    },
    "Insane": {
        "minimum": 0,
        "maximum": 1157,
        "icon": "🔴"
    }
}


# DIFFICULTY BUTTONS

st.subheader("Choose your difficulty")

diff_cols = st.columns(4)

difficulty_names = [
    "Normal",
    "Intermediate",
    "Advanced",
    "Insane"
]

for column, difficulty in zip(
    diff_cols,
    difficulty_names
):

    settings = difficulty_settings[difficulty]

    with column:

        if st.button(
            f"{settings['icon']} {difficulty}",
            key=f"number_game_difficulty_{difficulty}",
            use_container_width=True,
            disabled=st.session_state.number_game_active
        ):

            st.session_state.number_game_difficulty = difficulty
            st.session_state.number_game_won = None
            st.session_state.number_game_message = ""

            st.rerun()


# SELECTED DIFFICULTY

selected_difficulty = (
    st.session_state.number_game_difficulty
)

selected_settings = difficulty_settings[
    selected_difficulty
]

st.info(
    f"Selected: {selected_settings['icon']} "
    f"**{selected_difficulty}** — "
    f"Guess a number from "
    f"**{selected_settings['minimum']}** "
    f"to **{selected_settings['maximum']}**."
)


# NUMBER OF GUESSES

max_guesses = st.number_input(
    "❤️ Number of guesses",
    min_value=1,
    max_value=100,
    value=5,
    step=1,
    key="number_game_guess_limit",
    disabled=st.session_state.number_game_active
)


# START GAME

if st.button(
    "🚀 Start Game"
    if not st.session_state.number_game_active
    else "🔄 Restart Game",
    use_container_width=True
):

    st.session_state.number_game_secret = random.randint(
        selected_settings["minimum"],
        selected_settings["maximum"]
    )

    st.session_state.number_game_max_guesses = int(
        max_guesses
    )

    st.session_state.number_game_guesses_used = 0
    st.session_state.number_game_active = True
    st.session_state.number_game_won = None
    st.session_state.number_game_message = ""

    if "number_game_guess" in st.session_state:
        del st.session_state["number_game_guess"]

    st.rerun()


# GAMEPLAY

if st.session_state.number_game_active:

    st.markdown("---")

    guesses_left = (
        st.session_state.number_game_max_guesses
        - st.session_state.number_game_guesses_used
    )

    st.write(f"**Guesses remaining:** {guesses_left}")

    guess = st.number_input(
        f"Enter your guess "
        f"({selected_settings['minimum']}–"
        f"{selected_settings['maximum']})",
        min_value=selected_settings["minimum"],
        max_value=selected_settings["maximum"],
        step=1,
        key="number_game_guess"
    )

    if st.button(
        "🎯 Submit Guess",
        use_container_width=True
    ):

        st.session_state.number_game_guesses_used += 1

        secret = st.session_state.number_game_secret

        if int(guess) == secret:

            st.session_state.number_game_active = False
            st.session_state.number_game_won = True

            st.session_state.number_game_message = (
                "You found the secret number!"
            )

        elif (
            st.session_state.number_game_guesses_used
            >= st.session_state.number_game_max_guesses
        ):

            st.session_state.number_game_active = False
            st.session_state.number_game_won = False

            st.session_state.number_game_message = (
                "try harder next time little boy"
            )

        elif int(guess) < secret:

            st.session_state.number_game_message = (
                "📈 Too low! Try a higher number."
            )

        else:

            st.session_state.number_game_message = (
                "📉 Too high! Try a lower number."
            )

        st.rerun()

    if st.session_state.number_game_message:
        st.write(st.session_state.number_game_message)


# WINNING RESULTS

if st.session_state.number_game_won is True:

    st.markdown("---")

    st.success(
        f"🎉 Congratulations! The secret number was "
        f"**{st.session_state.number_game_secret}**. "
        f"You guessed it in "
        f"**{st.session_state.number_game_guesses_used}** "
        f"guess(es)! Amazing work! Keep challenging yourself!"
    )

    st.balloons()


# LOSING RESULTS

elif st.session_state.number_game_won is False:

    st.markdown("---")

    st.error(
        f"The secret number was "
        f"**{st.session_state.number_game_secret}**. "
        f"You used "
        f"**{st.session_state.number_game_guesses_used}** "
        f"guess(es). try harder next time little boy :>"
    )





# ==========================================
# MY TO-DO LIST
# ==========================================

st.markdown("---")

st.title("✅ My To-Do List")

st.write("Plan your day and track your progress.")


# ==========================================
# SESSION STATE
# ==========================================

if "todo_tasks" not in st.session_state:
    st.session_state.todo_tasks = []

if "todo_next_id" not in st.session_state:
    st.session_state.todo_next_id = 0

if "todo_error" not in st.session_state:
    st.session_state.todo_error = False


# ==========================================
# DELETE ONE TASK
# ==========================================

def delete_todo_task(task_id):

    st.session_state.todo_tasks = [
        task for task in st.session_state.todo_tasks
        if task["id"] != task_id
    ]

    checkbox_key = f"todo_done_{task_id}"

    if checkbox_key in st.session_state:
        del st.session_state[checkbox_key]


# ==========================================
# CLEAR ALL TASKS
# ==========================================

def clear_all_todo_tasks():

    for task in st.session_state.todo_tasks:

        checkbox_key = f"todo_done_{task['id']}"

        if checkbox_key in st.session_state:
            del st.session_state[checkbox_key]

    st.session_state.todo_tasks = []
    st.session_state.todo_error = False


# ==========================================
# TASK INPUT
# ==========================================

with st.form("todo_form", clear_on_submit=True):

    st.text_input(
        "What do you need to do?",
        placeholder="What do you need to do?",
        key="todo_input"
    )

    submitted = st.form_submit_button(
        "➕ Add Task",
        use_container_width=True
    )

    if submitted:

        task = st.session_state.todo_input.strip()

        if task:

            st.session_state.todo_tasks.append({
                "id": st.session_state.todo_next_id,
                "task": task
            })

            st.session_state.todo_next_id += 1
            st.session_state.todo_error = False

        else:

            st.session_state.todo_error = True


if st.session_state.todo_error:
    st.warning("Please enter a task first!")


# ==========================================
# TASK LIST
# ==========================================

st.markdown("---")

st.subheader("📋 My Tasks")


# CLEAR ALL BUTTON

st.button(
    "🧹 Clear All Tasks",
    on_click=clear_all_todo_tasks,
    disabled=len(st.session_state.todo_tasks) == 0,
    use_container_width=False
)


# ==========================================
# DISPLAY TASKS
# ==========================================

if st.session_state.todo_tasks:

    completed_tasks = 0

    for task in st.session_state.todo_tasks:

        task_id = task["id"]

        col1, col2 = st.columns([8, 1])

        # TASK CHECKBOX

        with col1:

            is_completed = st.checkbox(
                task["task"],
                key=f"todo_done_{task_id}"
            )

            if is_completed:
                completed_tasks += 1

        # DELETE BUTTON

        with col2:

            st.button(
                "🗑️",
                key=f"delete_todo_{task_id}",
                help="Delete this task",
                on_click=delete_todo_task,
                args=(task_id,)
            )


    # ======================================
    # PROGRESS BAR
    # ======================================

    total_tasks = len(st.session_state.todo_tasks)

    progress = completed_tasks / total_tasks

    st.markdown("---")

    st.subheader("📊 Your Progress")

    st.progress(progress)

    percentage = int(progress * 100)

    st.write(
        f"Completed {completed_tasks} "
        f"out of {total_tasks} tasks!"
    )

    st.caption(f"{percentage}% completed")


else:

    st.info("No tasks yet. Add your first task!")



# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="Student Money Manager",
    page_icon="💰",
    layout="centered"
)

# ==========================================
# SESSION STATE
# ==========================================

if "transactions" not in st.session_state:
    st.session_state.transactions = []

if "starting_balance" not in st.session_state:
    st.session_state.starting_balance = 0.0

if "money_next_id" not in st.session_state:
    st.session_state.money_next_id = 0

if "money_error" not in st.session_state:
    st.session_state.money_error = ""


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def add_transaction():

    description = st.session_state.money_description.strip()
    amount = float(st.session_state.money_amount)
    transaction_type = st.session_state.money_type
    transaction_date = st.session_state.money_date

    if not description:
        st.session_state.money_error = "Please enter a description."
        return

    if amount <= 0:
        st.session_state.money_error = "Please enter an amount greater than zero."
        return

    st.session_state.transactions.append({
        "id": st.session_state.money_next_id,
        "Date": transaction_date.isoformat(),
        "Description": description,
        "Type": transaction_type,
        "Amount": amount
    })

    st.session_state.money_next_id += 1
    st.session_state.money_error = ""


def delete_transaction(transaction_id):

    st.session_state.transactions = [
        transaction
        for transaction in st.session_state.transactions
        if transaction["id"] != transaction_id
    ]


def clear_transactions():

    st.session_state.transactions = []
    st.session_state.money_error = ""


# ==========================================
# HEADER
# ==========================================

st.title("💰 Student Money Manager")

st.write(
    "Keep track of your allowance, income, "
    "expenses, and savings."
)

st.markdown("---")


# ==========================================
# ALLOWANCE / STARTING BALANCE
# ==========================================

st.subheader("🏦 My Allowance")

st.number_input(
    "Starting balance / allowance (Rp)",
    min_value=0.0,
    step=1000.0,
    key="starting_balance",
    help="Enter the amount of money you currently have."
)


# ==========================================
# CALCULATE TOTALS
# ==========================================

income_total = sum(
    item["Amount"]
    for item in st.session_state.transactions
    if item["Type"] == "Income"
)

expense_total = sum(
    item["Amount"]
    for item in st.session_state.transactions
    if item["Type"] == "Expense"
)

current_balance = (
    st.session_state.starting_balance
    + income_total
    - expense_total
)


# ==========================================
# DASHBOARD SUMMARY
# ==========================================

st.markdown("---")

st.subheader("📊 Money Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "💵 Current Balance",
        f"Rp {current_balance:,.0f}"
    )

with col2:
    st.metric(
        "🎁 Starting Allowance",
        f"Rp {st.session_state.starting_balance:,.0f}"
    )

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "📈 Total Income",
        f"Rp {income_total:,.0f}"
    )

with col4:
    st.metric(
        "📉 Total Expenses",
        f"Rp {expense_total:,.0f}"
    )

if current_balance < 0:
    st.warning(
        "Your recorded expenses are higher than your available money."
    )

elif current_balance == 0:
    st.info("Your current balance is Rp 0.")


# ==========================================
# ADD TRANSACTION
# ==========================================

st.markdown("---")

st.subheader("➕ Add a Transaction")

with st.form("money_transaction_form", clear_on_submit=True):

    st.text_input(
        "Description",
        placeholder="e.g. Lunch, bus fare, pocket money",
        key="money_description"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.selectbox(
            "Transaction type",
            ["Expense", "Income"],
            key="money_type"
        )

    with col2:
        st.number_input(
            "Amount (Rp)",
            min_value=0.0,
            step=1000.0,
            key="money_amount"
        )

    st.date_input(
        "Date",
        value=date.today(),
        key="money_date"
    )

    submitted = st.form_submit_button(
        "Add Transaction",
        use_container_width=True
    )

    if submitted:

        add_transaction()

        if not st.session_state.money_error:
            st.success("Transaction added successfully!")
            st.rerun()


if st.session_state.money_error:
    st.warning(st.session_state.money_error)


# ==========================================
# TRANSACTION HISTORY
# ==========================================

st.markdown("---")

st.subheader("🧾 Transaction History")

if st.session_state.transactions:

    display_rows = []

    for item in st.session_state.transactions:

        display_rows.append({
            "Date": item["Date"],
            "Description": item["Description"],
            "Type": item["Type"],
            "Amount (Rp)": item["Amount"]
        })

    df = pd.DataFrame(display_rows)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # DELETE INDIVIDUAL TRANSACTIONS

    st.write("**Delete an individual transaction**")

    for item in reversed(st.session_state.transactions):

        col1, col2 = st.columns([5, 1])

        with col1:

            sign = "+" if item["Type"] == "Income" else "-"

            st.write(
                f"{item['Date']} · "
                f"{item['Description']} · "
                f"{item['Type']} · "
                f"{sign}Rp {item['Amount']:,.0f}"
            )

        with col2:

            st.button(
                "🗑️",
                key=f"delete_money_{item['id']}",
                help="Delete this transaction",
                on_click=delete_transaction,
                args=(item["id"],)
            )

    # DOWNLOAD CSV

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Transactions as CSV",
        data=csv_data,
        file_name="student_money_transactions.csv",
        mime="text/csv",
        use_container_width=True
    )

    # CLEAR ALL TRANSACTIONS

    st.button(
        "🧹 Clear All Transactions",
        on_click=clear_transactions,
        help="Remove all recorded transactions"
    )

else:

    st.info(
        "No transactions yet. Add your first income or expense above."
    )


# ==========================================
# SPENDING BREAKDOWN
# ==========================================

if expense_total > 0:

    st.markdown("---")

    st.subheader("📉 Spending Summary")

    st.write(
        f"You have recorded **Rp {expense_total:,.0f}** in expenses."
    )

    available_before_expenses = (
        st.session_state.starting_balance + income_total
    )

    if available_before_expenses > 0:

        spent_ratio = min(
            expense_total / available_before_expenses,
            1.0
        )

        st.progress(spent_ratio)

        st.caption(
            f"{spent_ratio * 100:.1f}% of your starting allowance "
            "and recorded income has been spent."
        )


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Tip: Record transactions regularly to keep your balance accurate."
)






