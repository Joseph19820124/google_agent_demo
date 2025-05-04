import google.cloud.dialogflowcx_v3beta1 as dialogflowcx

def main():
    # Initialize the Dialogflow CX client
    client = dialogflowcx.AgentsClient()

    # Define the agent
    agent = dialogflowcx.Agent(
        display_name="My Agent",
        default_language_code="en",
        time_zone="America/New_York"
    )

    # Create the agent
    response = client.create_agent(request={"agent": agent, "parent": "projects/my-project/locations/global"})
    print(f"Agent created: {response.name}")

if __name__ == "__main__":
    main()
