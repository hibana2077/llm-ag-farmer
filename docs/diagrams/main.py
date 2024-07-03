from diagrams import Diagram, Cluster
from diagrams.programming.framework import Svelte
from diagrams.onprem.client import Users
from diagrams.onprem.database import Cassandra
from diagrams.custom import Custom
from diagrams.onprem.monitoring import Grafana
from diagrams.programming.language import Python
from diagrams.programming.flowchart import Database
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.network import Internet
from diagrams.onprem.logging import Fluentbit

with Diagram("Hydroponic Farm System Architecture", show=False, direction="TB"):
    with Cluster("Core Components"):
        farmer_ai_agent = Python("Farmer AI Agent")
        human_interface = Svelte("Human Interface")
        farm_database = Cassandra("Farm Database")
        knowledge_base = Custom("Knowledge Base (GraphRAG)", "./resources/graph_rag.png")
    
    with Cluster("Peripheral Components"):
        farm_sensors = Custom("Farm Sensors", "./resources/arduino.png")
        farm_actuators = Custom("Farm Actuators", "./resources/arduino.png")
        weather_api = Custom("Weather API", "./resources/weather_api.png")  # Use a generic cloud icon
    
    users = Users("Farm Operators")
    
    users >> human_interface >> farmer_ai_agent
    farm_sensors >> farm_database >> farmer_ai_agent
    farmer_ai_agent >> farm_actuators
    weather_api >> farmer_ai_agent
    farmer_ai_agent >> knowledge_base