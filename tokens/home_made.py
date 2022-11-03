## importation
import re
import pandas as pd



def split_sentence(sentence):
    """
    Ultra basic, seems to work
    """

    ## parameters
    cleaned_sentence = []

    ## encoding
    string_encode = sentence.encode("ascii", "ignore")
    sentence = string_encode.decode()

    ## preprocess
    sentence = sentence.lower()
    sentence = sentence.replace(",", "")
    sentence = sentence.replace(".", "")
    sentence = sentence.replace("?", "")
    sentence = sentence.replace("!", "")
    sentence = sentence.replace("(", "")
    sentence = sentence.replace(")", "")
    sentence = sentence.replace("[", "")
    sentence = sentence.replace("]", "")
    sentence = sentence.replace("=", "")
    sentence = sentence.replace("+", "")
    sentence = sentence.replace("\"", "")
    sentence = sentence.replace("'", "")

    ## split sentence
    sentence = sentence.split(" ")
    
    ## loop over elt
    for elt in sentence:

        #-> init attribute
        elt_is_cleaned = True

        #-> remove short ones
        if(len(elt) < 2):
            elt_is_cleaned = False
        
        #-> remove numeric elt
        try:
            elt = float(elt)
            elt_is_cleaned = False
        except:
            pass

        #-> remove stupid terms
        if(elt in ["vr"]):
            elt_is_cleaned = False

        #-> evaluate attribute
        if(elt_is_cleaned):
            cleaned_sentence.append(elt)

    ## return clean sentence
    return cleaned_sentence




def spot_stop_words(vector):
    """
    """

    ## parameters
    token = "{stop-word}"
    tagged_vector = []
    target_list = ["the", "and", "or", "in"]

    ## clean the vector
    for elt in vector:
        if(elt in target_list):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector


def spot_intervention_words(vector):
    """
    """
    
    ## parameters
    token = "{intervention}"
    tagged_vector = []
    target_list = ["intervention", "interventional"]

    ## clean the vector
    for elt in vector:
        if(elt in target_list):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector


def spot_publication_material(vector):
    """
    """

    ## parameters
    token = "{publication-material}"
    tagged_vector = []
    target_list = ["paper", "table", "figure"]

    ## clean the vector
    for elt in vector:
        if(elt in target_list or elt+"s" in target_list):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector


def spot_group_word(vector):
    """
    """

    ## parameters
    token = "{group}"
    tagged_vector = []
    target_list = ["group", "cohort", "arm"]

    ## clean the vector
    for elt in vector:

        #-> remove "s" if its the last character
        if(elt[-1] == "s"):
            elt2 = elt[:-1]
        else:
            elt2 = elt

        if(elt2 in target_list):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector


def spot_control_word(vector):
    """
    """

    ## parameters
    token = "{ctrl}"
    tagged_vector = []
    target_list = ["control"]

    ## clean the vector
    for elt in vector:

        #-> remove "s" if its the last character
        if(elt[-1] == "s"):
            elt2 = elt[:-1]
        else:
            elt2 = elt

        if(elt2 in target_list):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector

def spot_comparison_words(vector):
    """
    """

    ## parameters
    token = "{comparison}"
    tagged_vector = []
    target_list = ["between", "versus", "vs", "more", "less"]
    target_list2 = ["comparison", "above", "below"]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list2):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector



def spot_differences_word(vector):
    """
    """

    ## parameters
    token = "{difference}"
    tagged_vector = []
    target_list = ["different", "difference", "other"]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector


def spot_significant_words(vector):
    """

    """

    ## parameters
    token = "{significant}"
    tagged_vector = []
    target_list = [
            "significant",
            "significative",
            "substantially",
            "substantial"
        ]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector


def spot_statistic_words(vector):
    """
    """

    ## parameters
    token = "{statistic}"
    tagged_vector = []
    target_list = ["statistic", "pval", "pvalue", "p-value", "statistically", "bayesian"]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector


def spot_negation_words(vector):
    """
    """
    
    ## parameters
    token = "{negative}"
    tagged_vector = []
    target_list = ["no", "not", "don't", "dont", "negative"]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector





def spot_be_words(vector):
    """
    """
    ## parameters
    token = "{be}"
    tagged_vector = []
    target_list = [
            "is",
            "are",
            "was",
            "were",
            "being"
        ]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector



def spot_indication_words(vector):
    """
    """
    ## parameters
    token = "{indication}"
    tagged_vector = []
    target_list = [
            "present",
            "presented",
            "indicate",
            "indicated",
            "indicating",
            "presenting",
            "seem",
            "show"
        ]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector



def spot_data_words(vector):
    """
    """
    ## parameters
    token = "{data}"
    tagged_vector = []
    target_list = [
            "data",
            "variable"
        ]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector



def spot_clinical_words(vector):
    """
    """
    ## parameters
    token = "{clinical}"
    tagged_vector = []
    target_list = [
            "clinical",
            "trial"
        ]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector




def spot_demographic_words(vector):
    """
    """
    ## parameters
    token = "{demographic}"
    tagged_vector = []
    target_list = [
            "demographic",
            "demographical"
        ]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector



def spot_patient_words(vector):
    """
    """
    
    ## parameters
    token = "{patient}"
    tagged_vector = []
    target_list = ["patient", "case"]

    ## clean the vector
    for elt in vector:

        #-> init attribute
        add_token = False

        #-> check target list 1
        if(elt in target_list):
            add_token = True

        #-> remove "s" if its the last character
        if(len(elt) > 1):
            if(elt[-1] == "s"):
                elt2 = elt[:-1]
            else:
                elt2 = elt
        else:
            add_token = False

        #-> check target list 2
        if(elt2 in target_list):
            add_token = True

        #-> update token
        if(add_token):
            tagged_vector.append(token)
        else:
            tagged_vector.append(elt)

    ## return cleaned vector
    return tagged_vector









def run():
    """
    
    """

    ## parameters
    data_file = "/home/panda/Workspace/Delphi_score/data/database_all.csv"

    ## load file
    df = pd.read_csv(data_file, encoding="utf-8")

    ## split sentence
    for index, row in df.iterrows():
        sentence = row["SENTENCE"]
        sequence = split_sentence(sentence)
        
        # tokenisation
        sequence = spot_stop_words(sequence)
        sequence = spot_intervention_words(sequence)
        sequence = spot_publication_material(sequence)
        sequence = spot_group_word(sequence)
        sequence = spot_control_word(sequence)
        sequence = spot_comparison_words(sequence)
        sequence = spot_differences_word(sequence)
        sequence = spot_significant_words(sequence)
        sequence = spot_statistic_words(sequence)
        sequence = spot_negation_words(sequence)
        sequence = spot_indication_words(sequence)
        sequence = spot_be_words(sequence)
        sequence = spot_data_words(sequence)
        sequence = spot_clinical_words(sequence)
        sequence = spot_demographic_words(sequence)
        sequence = spot_patient_words(sequence)


        # check results
        for elt in sequence:
            if(elt[0] != "{" or elt[-1] != "}"):
                print(elt)


run()

