import os
import argparse
import openai
import schedule
import time


def run_prompt(prompt: str, model: str = "gpt-3.5-turbo") -> None:
    """Send a prompt to the OpenAI API and print the response."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable not set")
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    answer = response.choices[0].message.content
    print(answer)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ChatGPT prompts on a schedule")
    parser.add_argument("prompt", help="The prompt text to send to ChatGPT")
    parser.add_argument("--time", default="09:00", help="Time of day to run (HH:MM)")
    parser.add_argument(
        "--daily", action="store_true", help="Run the prompt every day at the specified time"
    )
    parser.add_argument(
        "--weekly",
        metavar="DAY",
        help="Run the prompt weekly on the given day (e.g. monday) at the specified time",
    )
    parser.add_argument(
        "--once", action="store_true", help="Run the prompt a single time and exit"
    )
    parser.add_argument(
        "--model", default="gpt-3.5-turbo", help="Model name for OpenAI completion"
    )

    args = parser.parse_args()

    if args.once:
        run_prompt(args.prompt, args.model)
        return

    if args.daily:
        schedule.every().day.at(args.time).do(run_prompt, args.prompt, args.model)
    elif args.weekly:
        day = args.weekly.lower()
        if not hasattr(schedule.every(), day):
            raise ValueError(f"Invalid day of week: {args.weekly}")
        getattr(schedule.every(), day).at(args.time).do(
            run_prompt, args.prompt, args.model
        )
    else:
        parser.error("Either --daily, --weekly DAY, or --once must be specified")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
