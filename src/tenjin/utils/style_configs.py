import dash_bootstrap_components as dbc


INSTRUCTION_TEXT_SHARED = 'Click and drag on the graph to select the range of data points to inspect feature values.'
INSTRUCTION_TEXT_REG = 'To reset back to default settings, hover over icons on the top right of the graph and click "Autoscale" icon.'
WARNING_TEXT = 'To inspect new range of datapoints in different graph, please first reset the earlier selection by clicking "Autoscale" icon ' \
                'at the top right corner of the graph.'

DEFAULT_HEADER_STYLE = {'fontWeight': 'bold', 'color': 'white', 'backgroundColor': '#7e746d', 'border': '1px solid rgb(229, 211, 197)'}
DEFAULT_TITLE_STYLE = {'visibility': 'visible'}
DEFAULT_PLOT_NAME_STYLE = {'visibility': 'visible'}


def default_header_style():
    DEFAULT_HEADER_STYLE['visibility'] = 'visible'
    return DEFAULT_HEADER_STYLE


def collapse_header_style():
    DEFAULT_HEADER_STYLE['border'] = 'none'
    DEFAULT_HEADER_STYLE['visibility'] = 'collapse'
    return DEFAULT_HEADER_STYLE


def dummy_alert():
    alert_obj = dbc.Alert(color="light", style={'visibility': 'hidden'})
    return alert_obj


def activate_alert():
    alert_obj = dbc.Alert(INSTRUCTION_TEXT_REG, color="secondary", className='alert__note-reg')
    return alert_obj