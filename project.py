
import streamlit as st

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


