import streamlit as st

# Sample data for tasks
tasks_data = [
    {'id': 1, 'title': 'Drink Water', 'description': 'Stay hydrated throughout the day.'},
    {'id': 2, 'title': 'Exercise', 'description': 'Engage in physical activity.'},
    {'id': 3, 'title': 'Meditate', 'description': 'Practice mindfulness and relaxation.'},
]

# Function to display health parameters
def display_health():
    st.title("Health Parameters")
    st.write("Heart Rate: 72 bpm")
    st.write("Steps: 5000")
    st.write("Calories Burned: 300")
    st.button("Start Workout")
    st.button("Track Sleep")
    st.button("View History")

# Function to display health resources
def display_health_site():
    st.title("Health Resources")
    st.write("Find articles and resources to improve your health.")
    # You can add links or resources here

# Function to display tasks
def display_tasks():
    st.title("Health Tasks")
    for task in tasks_data:
        if st.button(task['title']):
            display_task_detail(task)

# Function to display task details
def display_task_detail(task):
    st.subheader(task['title'])
    st.write(task['description'])
    st.write("### Sub Tasks")
    st.write("1. Voice Note: [Record your voice note]")
    st.write("2. Paragraph: [Write a paragraph about the task]")
    st.write("3. About the Task: [More information about the task]")
    if st.button("Back to Tasks"):
        display_tasks()

# Main application logic
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose a module", ["Health", "Health Site", "Tasks"])

    if app_mode == "Health":
        display_health()
    elif app_mode == "Health Site":
        display_health_site()
    elif app_mode == "Tasks":
        display_tasks()

if __name__ == "__main__":
    main()
