"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config
from Foodify_La_hacks.model import get_intial_request
import reflex as rx

# from chatapp import style

class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        answer = get_intial_request(self.question)
        self.chat_history.append((self.question, answer))


shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
    max_width="50em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4),
)
answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("accent", 8),
)

heading_style = dict(
    font_size="40px",
    font_color=rx.color("purple", 8),
    font_weight="bold",
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", 
    padding="1em", 
    box_shadow=shadow,
    width="220px",

)
button_style = dict(
    background_color=rx.color("accent", 10),
    box_shadow=shadow,
)


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_change=State.set_question,
            style=input_style,
        ),
        rx.button(
            "Reply",
            on_click=State.answer,
            style=button_style,
        ),
    )


def bot() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
            height="100%",
        ),
        
    )

def index() -> rx.Component:
    return rx.vstack(
        rx.text("Foodify! Simplify Food Search", style=heading_style),
        rx.button("Open AI",
        border_radius="1em",
        box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
        background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
        box_sizing="border-box",
        color="white",
        opacity=1,
        on_click=rx.redirect(
            "/bot"
        ),
        _hover={
            "opacity": 0.5,},
        ),
        align="center",
        background_color=rx.color("sand", 7),
        height="100vh",
        padding_top="40vh"

    )


app = rx.App()
app.add_page(index)
app.add_page(bot)
