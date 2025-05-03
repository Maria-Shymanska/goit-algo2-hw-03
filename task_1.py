import networkx as nx
import pandas as pd

# Function to create the logistics graph
def create_logistics_graph():
    G = nx.DiGraph()  # Create a directed graph

    # Add the source and sink nodes
    G.add_node("source")
    G.add_node("sink")

    # Connect the source to terminals with capacities
    G.add_edge("source", "T1", capacity=1000)
    G.add_edge("source", "T2", capacity=1000)

    # Terminals to warehouses connections with capacities
    G.add_edge("T1", "S1", capacity=25)
    G.add_edge("T1", "S2", capacity=20)
    G.add_edge("T1", "S3", capacity=15)
    G.add_edge("T2", "S3", capacity=15)
    G.add_edge("T2", "S4", capacity=30)
    G.add_edge("T2", "S2", capacity=10)

    # Warehouses to stores connections with capacities
    G.add_edge("S1", "M1", capacity=15)
    G.add_edge("S1", "M2", capacity=10)
    G.add_edge("S1", "M3", capacity=20)

    G.add_edge("S2", "M4", capacity=15)
    G.add_edge("S2", "M5", capacity=10)
    G.add_edge("S2", "M6", capacity=25)

    G.add_edge("S3", "M7", capacity=20)
    G.add_edge("S3", "M8", capacity=15)
    G.add_edge("S3", "M9", capacity=10)

    G.add_edge("S4", "M10", capacity=20)
    G.add_edge("S4", "M11", capacity=10)
    G.add_edge("S4", "M12", capacity=15)
    G.add_edge("S4", "M13", capacity=5)
    G.add_edge("S4", "M14", capacity=10)

    # Connect the stores to the sink with large capacities
    for i in range(1, 15):
        G.add_edge(f"M{i}", "sink", capacity=1000)

    return G  # Return the constructed graph

# Build the graph and calculate the maximum flow
G = create_logistics_graph()
flow_value, flow_dict = nx.maximum_flow(G, "source", "sink", flow_func=nx.algorithms.flow.edmonds_karp)

# Print the maximum flow value
print(f"🔢 Maximum flow: {flow_value}\n")

# Build a table: Terminal → Store flow
results = []

# Determine paths from terminals to stores
for terminal in ["T1", "T2"]:
    for warehouse in flow_dict[terminal]:
        if flow_dict[terminal][warehouse] > 0:
            for store in flow_dict[warehouse]:
                actual_flow = flow_dict[warehouse][store]
                if actual_flow > 0:
                    # Add the results to the list
                    results.append({
                        "Terminal": terminal,
                        "Store": store,
                        "Actual Flow (units)": actual_flow
                    })

# Create and print the DataFrame
df = pd.DataFrame(results)
print(df.to_string(index=False))

