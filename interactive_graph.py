
import plotly.graph_objects as go
import networkx as nx 

class CreatePlotlyViz:

    def __init__(self,G):
        self.G = G
        self.layout = nx.spring_layout(G)

    def edge_trace(self):            
        '''
        Input: G: networkx graph 
        Output: edge_trace
        '''
        edge_x = []
        edge_y = []
        for edge in self.G.edges():
            x0,y0 = self.layout[edge[0]]
            x1,y1 = self.layout[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
        return go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')
        
    def node_trace(self):
        node_x = []
        node_y = []
        for node in self.G.nodes():
            x, y = self.layout[node]
            node_x.append(x)
            node_y.append(y)

        return go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YlGnBu',
                reversescale=True,
                color=[],
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2))



    def node_label_color(self):
        node_adjacencies = []
        node_text = []
        for node, adjacencies in self.G.adjacency():
            node_adjacencies.append(len(adjacencies))
            node_text.append(f'{node} : {len(adjacencies)}')
        return node_adjacencies, node_text

    def fig(self, width = 800, height = 800):
        edge_trace = self.edge_trace()
        node_trace = self.node_trace()
        node_trace.marker.color, node_trace.text = self.node_label_color()
        fig = go.Figure(data=[edge_trace, node_trace],
            layout=go.Layout(
            width = width,
            height = height,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
            )
        fig.show()
               
