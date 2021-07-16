import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import sys

from ..interpreters.structured_data import GeneralMetrics
from ..visualizer import general_metrics as viz_general



def fig_confusion_matrix(data_loader):
    """
    Create confusion matrix
    
    Arguments:
        data_loader {class object} 
        -- output from data loader pipeline 
    
    Returns:
        plotly graph 
        -- displaying confusion matrix details
    """
    yTrue, yPred, model_names = GeneralMetrics(data_loader, 'confMat').xform()
    fig_objs = viz_general.plot_confusion_matrix(yTrue, yPred, model_names)
    return fig_objs


def fig_classification_report(data_loader):
    """
    Create classification report in table form
    
    Arguments:
        data_loader {class object} 
        -- output from data loader pipeline 
    
    Returns:
        plotly table 
        -- containing classification report details
    """
    yTrue, yPred, model_names = GeneralMetrics(data_loader, 'classRpt').xform()
    fig_objs = viz_general.plot_classification_report(yTrue, yPred, model_names)
    return fig_objs


def fig_roc_curve(data_loader):
    """
    Display roc curve for comparison on various models
    
    Arguments:
        data_loader {class object} 
        -- output from data loader pipeline 
    
    Returns:
        plotly line curve 
        -- comparing roc-auc score for various models
    """
    yTrue, yPred, model_names = GeneralMetrics(data_loader, 'rocAuc').xform()
    fig_obj = viz_general.plot_roc_curve(yTrue, yPred, model_names)
    return fig_obj


def fig_precisionRecall_curve(data_loader):
    """
    Display precision-recall curve for comparison on various models
    
    Arguments:
        data_loader {class object} 
        -- output from data loader pipeline 
    
    Returns:
        plotly line curve 
        -- comparing roc-auc score for various models
    """
    yTrue, yPred, model_names = GeneralMetrics(data_loader, 'precRecall').xform()
    fig_obj = viz_general.plot_precisionRecall_curve(yTrue, yPred, model_names)
    return fig_obj


class GenericMetrics:
    def __init__(self, data_loader):
        self.data_loader = data_loader
        self.conf_matrix = fig_confusion_matrix(self.data_loader)
        self.cls_report = fig_classification_report(self.data_loader)
        self.roc = fig_roc_curve(self.data_loader)
        self.prec_recall = fig_precisionRecall_curve(self.data_loader)

    def show(self):
        if len(self.conf_matrix) > 1:
            gen_metrics = dbc.Container([
                                dbc.Row([
                                    dbc.Col([
                                        dcc.Graph(figure=self.conf_matrix[0]),
                                        dcc.Graph(figure=self.cls_report[0]),
                                        ], className="border__common"), 

                                    dbc.Col([
                                        dcc.Graph(figure=self.conf_matrix[1]),
                                        dcc.Graph(figure=self.cls_report[1]),
                                        ], className="border__common")
                                    ]), 

                                html.Div(html.Div(dcc.Graph(figure=self.roc), className="fig__roc-prec-recall"), className="border__common"),
                                html.Div(html.Div(dcc.Graph(figure=self.prec_recall), className="fig__roc-prec-recall"), className="border__common")
                        ], fluid=True)

        elif len(self.conf_matrix) == 1:
            gen_metrics = dbc.Container([
                                html.Div(dbc.Row([
                                    dbc.Col(dcc.Graph(figure=self.conf_matrix[0]), className="border__common"), 
                                    dbc.Col(dcc.Graph(figure=self.cls_report[0]), className="border__common")
                                    ]), className="boundary__common"), 

                                html.Div(html.Div(dcc.Graph(figure=self.roc), className="fig__roc-prec-recall"), className="border__common"),
                                html.Div(html.Div(dcc.Graph(figure=self.prec_recall), className="fig__roc-prec-recall"), className="border__common")
                        ], fluid=True, className="boundary__common")

        return gen_metrics