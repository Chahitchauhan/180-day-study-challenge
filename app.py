import streamlit as st
import json
import os
from datetime import date, timedelta


# ============================================================
# APP SETTINGS
# ============================================================

TOTAL_DAYS = 180
DAILY_TARGET = 3.0
DATA_FILE = "study_data.json"


# ============================================================
# DAILY BUSINESS / FINANCE INSIGHTS
# ============================================================

INSIGHTS = [
    ("Warren Buffett", "Think long term. Compounding becomes powerful when you give it time."),
    ("Charlie Munger", "Avoiding major mistakes can be just as important as finding great opportunities."),
    ("Peter Lynch", "Understand what you are investing in before putting your money behind it."),
    ("Benjamin Graham", "Price and value are not always the same thing."),
    ("Howard Marks", "Risk is more than volatility. Think about the possibility of permanent loss."),
    ("Ray Dalio", "Learn from mistakes and turn those lessons into principles."),
    ("Peter Drucker", "What gets measured can be managed and improved."),
    ("James Clear", "Small improvements repeated consistently can create remarkable results."),
    ("Naval Ravikant", "Build specific knowledge that becomes valuable in the marketplace."),
    ("Bill Gates", "Keep learning because technology and the world keep changing."),
    ("Jeff Bezos", "Customer needs can remain stable even when technology changes."),
    ("Indra Nooyi", "Long-term thinking means balancing today's performance with tomorrow's needs."),
    ("Ratan Tata", "Reputation is an asset that takes years to build."),
    ("N. R. Narayana Murthy", "Strong institutions are built on trust and discipline."),
    ("Azim Premji", "Financial discipline creates resilience."),
    ("Dhirubhai Ambani", "Think big, but build the capability required to execute."),
    ("Kiran Mazumdar-Shaw", "Innovation requires patience, experimentation and resilience."),
    ("Jack Ma", "Early setbacks do not necessarily determine the final outcome."),
    ("Satya Nadella", "A learning mindset can be more valuable than pretending to know everything."),
    ("Sundar Pichai", "Technology careers reward people who continue learning."),
    ("Sam Walton", "Pay attention to customers and understand what they actually want."),
    ("Michael Bloomberg", "Information becomes valuable when it improves decisions."),
    ("Michael Dell", "Business models determine how value is delivered."),
    ("Elon Musk", "Break complicated problems into smaller fundamental questions."),
    ("Sara Blakely", "Failure can provide information that helps you improve."),
    ("Brian Chesky", "Good products start with understanding the customer's experience."),
    ("Reed Hastings", "Strong organizations continuously examine whether their systems work."),
    ("Oprah Winfrey", "Build skills and credibility before expecting large opportunities."),
    ("Dhirubhai Ambani", "Ambition needs execution to become a business result."),
    ("Kiran Mazumdar-Shaw", "Difficult problems can create valuable opportunities for innovation."),
    ("Warren Buffett", "Read widely. Better decisions usually require better mental models."),
    ("Charlie Munger", "Know the limits of your own knowledge."),
    ("Peter Lynch", "Research creates conviction; headlines often create emotion."),
    ("Benjamin Graham", "Investment decisions should be based on analysis rather than excitement."),
    ("Howard Marks", "Good risk management starts before the risk becomes obvious."),
    ("Ray Dalio", "Pain plus reflection can become progress."),
    ("Peter Drucker", "Focus on effectiveness, not simply being busy."),
    ("James Clear", "Consistency beats occasional bursts of motivation."),
    ("Naval Ravikant", "Leverage can multiply the output of your time and skills."),
    ("Bill Gates", "Deep learning creates advantages that are difficult to copy quickly."),
    ("Jeff Bezos", "Long-term thinking changes how companies make decisions."),
    ("Elon Musk", "Question whether a rule is fundamental or simply a historical habit."),
    ("Sam Walton", "Listen carefully to customers and employees."),
    ("Michael Dell", "Strong execution turns strategy into measurable outcomes."),
    ("Michael Bloomberg", "Better information can reduce uncertainty in decision-making."),
    ("Indra Nooyi", "Good strategy balances short-term execution with long-term direction."),
    ("Ratan Tata", "Business relationships are built through consistency and trust."),
    ("N. R. Narayana Murthy", "Professionalism and transparency can support long-term growth."),
    ("Azim Premji", "Capital should be allocated with discipline."),
    ("Jack Ma", "Adaptability can matter more than having a perfect initial plan."),
    ("Satya Nadella", "Curiosity helps organizations adapt."),
    ("Sundar Pichai", "Good technology should ultimately solve a useful problem."),
    ("Warren Buffett", "Patience can be a competitive advantage."),
    ("Charlie Munger", "Simple mental models can improve complex decisions."),
    ("Peter Lynch", "Know why you own an investment."),
    ("Benjamin Graham", "Do not confuse a rising price with a better business."),
    ("Howard Marks", "Cycles matter. Good decisions consider where you are in the cycle."),
    ("Ray Dalio", "Write down what went wrong so the lesson becomes reusable."),
    ("Peter Drucker", "Strategy also means deciding what not to do."),
    ("James Clear", "Make progress visible and your habits easier to maintain."),
    ("Naval Ravikant", "Choose opportunities where your unique knowledge creates leverage."),
    ("Bill Gates", "Technology is powerful when it is applied to real problems."),
    ("Jeff Bezos", "Customer obsession can guide product decisions."),
    ("Elon Musk", "Challenge assumptions before accepting constraints."),
    ("Sam Walton", "Small operational improvements can compound across a large organization."),
    ("Michael Dell", "Cash flow and operational efficiency matter to business survival."),
    ("Michael Bloomberg", "Data becomes useful when it leads to better decisions."),
    ("Indra Nooyi", "Leadership requires thinking beyond the immediate quarter."),
    ("Ratan Tata", "Long-term value sometimes requires decisions that are not immediately rewarded."),
    ("N. R. Narayana Murthy", "Trust can become one of the strongest assets of an organization."),
    ("Azim Premji", "A strong balance sheet can provide flexibility during uncertainty."),
    ("Kiran Mazumdar-Shaw", "Innovation rarely happens without experimentation."),
    ("Jack Ma", "Customers can teach you things that planning alone cannot."),
    ("Satya Nadella", "Empathy can improve leadership and product design."),
    ("Sundar Pichai", "Keep building skills that remain useful as tools change."),
    ("Warren Buffett", "A good business can be more valuable than a complicated business."),
    ("Charlie Munger", "Avoid situations where one mistake can permanently destroy capital."),
    ("Peter Lynch", "Do the research instead of following market excitement."),
    ("Benjamin Graham", "Use facts and analysis to protect yourself from emotional decisions."),
    ("Howard Marks", "Uncertainty is unavoidable, so prepare for multiple scenarios."),
    ("Ray Dalio", "Create principles from your experiences so you can reuse the lessons."),
    ("Peter Drucker", "Results matter more than activity alone."),
    ("James Clear", "Track progress because visible progress helps maintain habits."),
    ("Naval Ravikant", "Build assets that can create value beyond your hours."),
    ("Bill Gates", "The ability to learn quickly can become a lifelong advantage."),
    ("Jeff Bezos", "Long-term customer trust can be more valuable than short-term optimization."),
    ("Elon Musk", "Break problems down to their fundamental components."),
    ("Sam Walton", "Execution at scale depends on thousands of small decisions."),
    ("Michael Dell", "Efficiency can create room for growth."),
    ("Michael Bloomberg", "Good data is a foundation for good analysis."),
    ("Indra Nooyi", "Strong leadership requires both performance and responsibility."),
    ("Ratan Tata", "Leadership includes responsibility for the consequences of decisions."),
    ("N. R. Narayana Murthy", "Strong ethics can support durable institutions."),
    ("Azim Premji", "Long-term wealth creation requires discipline."),
    ("Dhirubhai Ambani", "Large opportunities often require unconventional thinking."),
    ("Kiran Mazumdar-Shaw", "Technical knowledge becomes commercially valuable when paired with execution."),
    ("Jack Ma", "Adaptability is valuable when circumstances change."),
    ("Satya Nadella", "Learning from others can accelerate personal growth."),
    ("Sundar Pichai", "Stay curious about how technology changes industries."),
    ("Warren Buffett", "The best investment you can make is often improving your own capabilities."),
    ("Charlie Munger", "Temperament can matter as much as intelligence in investing."),
    ("Peter Lynch", "Understand the numbers behind the story."),
    ("Benjamin Graham", "Protect capital before chasing returns."),
    ("Howard Marks", "Think about what can go wrong before assuming what can go right."),
    ("Ray Dalio", "Principles become valuable when they guide action."),
    ("Peter Drucker", "Priorities require saying no to some things."),
    ("James Clear", "Consistency creates momentum."),
    ("Naval Ravikant", "Build skills that are difficult to replace."),
    ("Bill Gates", "Continuous learning creates long-term adaptability."),
    ("Jeff Bezos", "Think long term while executing today."),
    ("Elon Musk", "Question assumptions before accepting constraints."),
    ("Sam Walton", "Small improvements matter at scale."),
    ("Michael Dell", "Cash flow keeps businesses alive."),
    ("Michael Bloomberg", "Data should improve decisions."),
    ("Indra Nooyi", "Think about the next decade while executing this quarter."),
    ("Ratan Tata", "Long-term relationships can create long-term value."),
    ("N. R. Narayana Murthy", "Trust is a business asset."),
    ("Azim Premji", "Resilience comes from disciplined decisions."),
    ("Dhirubhai Ambani", "Think beyond the obvious opportunity."),
    ("Kiran Mazumdar-Shaw", "Persistence is part of innovation."),
    ("Jack Ma", "Adaptation is a business skill."),
    ("Satya Nadella", "Stay a student."),
    ("Sundar Pichai", "Keep learning as tools evolve."),
]


# ============================================================
# DATA FUNCTIONS
# ============================================================

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            pass

    return {
        "start_date": str(date.today()),
        "entries": {}
    }


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="180-Day Job Ready Journey",
    page_icon="🚀",
    layout="wide"
)


# ============================================================
# LOAD USER DATA
# ============================================================

if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data

if "start_date" not in data:
    data["start_date"] = str(date.today())

if "entries" not in data:
    data["entries"] = {}

save_data(data)

start_date = date.fromisoformat(data["start_date"])
today = date.today()

day_number = (today - start_date).days + 1

if day_number < 1:
    day_number = 1

if day_number > TOTAL_DAYS:
    day_number = TOTAL_DAYS

days_left = TOTAL_DAYS - day_number
progress = day_number / TOTAL_DAYS


# ============================================================
# TITLE
# ============================================================

st.title("🚀 My 180-Day Job Ready Journey")

st.caption(
    "One day • One skill • One step closer to becoming job-ready."
)


# ============================================================
# TOP DASHBOARD
# ============================================================

entries = data["entries"]

total_hours = sum(
    float(item.get("hours", 0))
    for item in entries.values()
)

study_days = len(entries)

average_hours = (
    total_hours / study_days
    if study_days > 0
    else 0
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📅 Journey Day",
        f"{day_number} / {TOTAL_DAYS}"
    )

with col2:
    st.metric(
        "⏳ Days Remaining",
        days_left
    )

with col3:
    st.metric(
        "🎯 Daily Target",
        f"{DAILY_TARGET:.1f} hrs"
    )

with col4:
    st.metric(
        "⏱️ Total Study",
        f"{total_hours:.1f} hrs"
    )


# ============================================================
# JOURNEY PROGRESS
# ============================================================

st.subheader(
    f"🗺️ Journey Progress — {progress * 100:.1f}%"
)

st.progress(progress)


# ============================================================
# PLAYFUL ROAD
# ============================================================

st.subheader("🛣️ Your Journey")

# Divide the road into 10 sections.
road_parts = 10

current_part = min(
    road_parts - 1,
    int(progress * road_parts)
)

road_columns = st.columns(road_parts)

for index, column in enumerate(road_columns):

    with column:

        if index == current_part:
            st.markdown("### 🧑‍💻")
        elif index < current_part:
            st.markdown("### 🟢")
        else:
            st.markdown("### ⚪")

        st.caption(
            f"Day {int(index * TOTAL_DAYS / road_parts) + 1}"
        )

st.progress(progress)

st.caption(
    f"🏁 Start: Day 1                                      🎯 Finish: Day {TOTAL_DAYS}"
)


# ============================================================
# DAILY BUSINESS INSIGHT
# ============================================================

author, insight = INSIGHTS[
    (day_number - 1) % len(INSIGHTS)
]

st.subheader("💡 Today's Business / Finance Insight")

st.info(
    f"**{insight}**\n\n"
    f"— {author}"
)

st.caption(
    "Note: These are learning insights and paraphrases, "
    "not necessarily verbatim quotations."
)


# ============================================================
# TODAY'S STUDY SESSION
# ============================================================

st.subheader("📚 Today's Study Session")

today_key = str(today)

existing = entries.get(today_key, {})

hours = st.number_input(
    "⏱️ How many hours did you study today?",
    min_value=0.0,
    max_value=24.0,
    value=float(existing.get("hours", 0)),
    step=0.5
)

topics = st.text_area(
    "📚 What topics did you cover?",
    value=existing.get("topics", ""),
    placeholder=(
        "Example: Python loops, functions, lists, SQL..."
    )
)

learning = st.text_area(
    "🧠 What did you learn?",
    value=existing.get("learning", ""),
    placeholder=(
        "Write the important things you understood today..."
    )
)

comments = st.text_area(
    "💬 Comments / Thoughts",
    value=existing.get("comments", ""),
    placeholder=(
        "What was easy? What was difficult? "
        "What do you want to revise?"
    )
)


# ============================================================
# SAVE PROGRESS
# ============================================================

if st.button(
    "💾 Save Today's Progress",
    type="primary",
    use_container_width=True
):

    entries[today_key] = {
        "day": day_number,
        "hours": hours,
        "topics": topics,
        "learning": learning,
        "comments": comments
    }

    data["entries"] = entries

    save_data(data)

    st.session_state.data = data

    st.success(
        "🎉 Today's progress has been saved!"
    )

    if hours >= DAILY_TARGET:

        st.balloons()

        st.success(
            f"🔥 Amazing! You completed your "
            f"{DAILY_TARGET:.1f}-hour target!"
        )

    elif hours > 0:

        remaining = DAILY_TARGET - hours

        st.info(
            f"💪 You studied {hours:.1f} hours. "
            f"Only {remaining:.1f} hours left to reach today's target."
        )


# ============================================================
# STREAK CALCULATION
# ============================================================

st.subheader("🔥 Your Streak")

streak = 0
check_date = today

while str(check_date) in entries:

    hours_done = float(
        entries[str(check_date)].get("hours", 0)
    )

    if hours_done > 0:

        streak += 1
        check_date -= timedelta(days=1)

    else:

        break


# ============================================================
# XP POINTS
# ============================================================

points = 0

for item in entries.values():

    studied = float(
        item.get("hours", 0)
    )

    if studied > 0:
        points += 10

    if studied >= DAILY_TARGET:
        points += 20

    if item.get("topics", "").strip():
        points += 5

    if item.get("learning", "").strip():
        points += 5

    if item.get("comments", "").strip():
        points += 5


s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric(
        "🔥 Current Streak",
        f"{streak} days"
    )

with s2:
    st.metric(
        "⭐ XP Points",
        points
    )

with s3:
    st.metric(
        "📚 Study Days",
        study_days
    )

with s4:
    st.metric(
        "📈 Average",
        f"{average_hours:.1f} hrs/day"
    )


# ============================================================
# LEVEL SYSTEM
# ============================================================

level = (points // 100) + 1
level_progress = (points % 100) / 100

st.subheader(
    f"🎮 Level {level}"
)

st.progress(level_progress)

st.caption(
    f"{points % 100}/100 XP toward Level {level + 1}"
)


# ============================================================
# ACHIEVEMENTS
# ============================================================

st.subheader("🏆 Achievements")

a1, a2, a3, a4 = st.columns(4)

with a1:

    if streak >= 7:
        st.success("🔥 7-Day Streak")
    else:
        st.info("🔒 7-Day Streak")

with a2:

    if streak >= 30:
        st.success("🔥 30-Day Streak")
    else:
        st.info("🔒 30-Day Streak")

with a3:

    if total_hours >= 100:
        st.success("💯 100 Study Hours")
    else:
        st.info("🔒 100 Study Hours")

with a4:

    if day_number >= 180:
        st.success("🏆 180 Days Complete")
    else:
        st.info("🔒 Day 180")


# ============================================================
# STUDY HISTORY
# ============================================================

st.divider()

st.subheader("📖 Study History")

if entries:

    sorted_entries = sorted(
        entries.items(),
        reverse=True
    )

    for entry_date, item in sorted_entries[:30]:

        hours_value = item.get("hours", 0)

        with st.expander(
            f"📅 {entry_date}  •  ⏱️ {hours_value} hrs"
        ):

            st.write(
                f"**Journey Day:** "
                f"{item.get('day', '-')}"
            )

            st.write(
                f"**📚 Topics:** "
                f"{item.get('topics', 'Not recorded')}"
            )

            st.write(
                f"**🧠 What I learned:** "
                f"{item.get('learning', 'Not recorded')}"
            )

            st.write(
                f"**💬 Comments:** "
                f"{item.get('comments', 'Not recorded')}"
            )

else:

    st.info(
        "🌱 Your journey starts here. "
        "Complete your first study session!"
    )


# ============================================================
# SETTINGS
# ============================================================

st.divider()

with st.expander("⚙️ Journey Settings"):

    st.write(
        f"📅 Journey start date: **{data['start_date']}**"
    )

    st.write(
        "💾 Your study data is stored locally "
        "in `study_data.json`."
    )

    st.warning(
        "Reset only if you intentionally want "
        "to start a new 180-day journey."
    )

    if st.button("🔄 Start New 180-Day Journey"):

        new_data = {
            "start_date": str(date.today()),
            "entries": {}
        }

        save_data(new_data)

        st.session_state.data = new_data

        st.success(
            "🚀 New 180-day journey started!"
        )

        st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🚀 180 Days • 📚 Daily Learning • 🔥 Consistency • 🎯 Job Ready"
)

st.caption(
    "Progress over perfection."
)