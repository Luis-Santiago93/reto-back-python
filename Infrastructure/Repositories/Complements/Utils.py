import json
from dateutil.parser import parse
from sqlalchemy.orm import class_mapper


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def json_data_match(json_data=None, key=None, value=None):
    result = False
    if json_data.get(key, '') != '':
        result = json_data.get(key) == value
    return result

def serialize(model):
    """Transforms a model into a dictionary which can be dumped to JSON."""
    # first we get the names of all the columns on your model
    columns = [c.key for c in class_mapper(model.__class__).columns]

    #del columns['fecha_creacion']
    # then we return their values in a dict
    result= dict((c, getattr(model, c)) for c in columns)

    return result


def validate_duplicates(data):
    result = []
    for item in data:
        if item not in result:
            result.append(item)
        else:
            return False
    return True

list_default=[
        812012,2226011,2226014,2835001,2835002,2835003,2835077,2835092,2835113,2835114,
        2835115,2835630,2835631,2835632,2835633,2835639,2835693,2835891,2835938,2835947,
        2835948,2835951,2835952,2835953,2835969,2835972,2836022,2836028,2836029,2836030,
        2836031,2836868,2836869,2836872,2836908,2836911,2836912,2836914,2836915,2836916,
        2836917,2836920,2836921,2836922,2836923,2836924,2836926,2836927,2836928,2836931,
        2836932,2836934,2836935,2836936,2836937,2836938,2836939,2836940,2836941,2836942,
        2836946,2836971,2836973,2836974,2837072,2837078,2835004,2835036,2835076,2835412,
        2835683,2835725,2835787,2835858,2836644,2836645,2836849,2836851,2836871,2836909,
        2836910,2836913,2836918,2836919,2836925,2836929,2836930,2836943,3000000,3000002,
        3000003,3000004,3000005,3000006,3000007,3000008,3000009,3000010,3000011,3000012,
        3000013,3000014,3000015,3000016,3000017,3000018,3000019,3000020,3000021,3000022,
        3000023,3000024,3000025,3000026,3000027,3000028,3000044,3000070,3000071,3000072,
        3000079,3000086,3000089,3000090,3000113,
    ]
