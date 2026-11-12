from dotenv import load_dotenv

from agents.supervisor_agent import create_supervisor


load_dotenv(override=True, verbose=True)


def main():

    supervisor = create_supervisor()

    print("\nCredit Card Collections Assistant")
    print("Type 'exit' to stop.\n")

    # The whole conversation is sent on every turn, so the
    # supervisor remembers who the customer is and what was said.
    messages = []

    while True:

        customer_message = input("Customer: ")

        if customer_message.lower() == "exit":
            break

        messages.append({
            "role": "user",
            "content": customer_message
        })

        response = supervisor.invoke({
            "messages": messages
        })

        messages = response["messages"]

        print("\nSupervisor:")

        print(messages[-1].content)

        print("\n" + "-" * 60)


if __name__ == "__main__":
    main()
