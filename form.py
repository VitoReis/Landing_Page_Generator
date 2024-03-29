from auth import authentication
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools
from htmlReader import siteTitle, menuColor, cardColor, textColor, backgroundImage, whatsapp, productName,\
     productNameCount, productDescription, productDescriptionCount, productPrice, productPriceCount, productImage,\
     productImageCount

SCOPES = "https://www.googleapis.com/auth/drive"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"


def generate():
    creds = authentication()

    form_service = build('forms', 'v1', credentials=creds)

    # Request body for creating a form
    NEW_FORM = {
        "info": {
            "title": "Landing Page Questions",
            "description": "Preencha este formulario para gerar seu site.",
        }
    }

    # Request body to add a multiple-choice question
    NEW_QUESTION = {
        "requests": [{
            "createItem": {
                "item": {
                    "title": "Escolha um dos templates para o seu site",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [
                                    {"value": "1"},
                                ],
                                "shuffle": False
                            }
                        }
                    },
                },
                "location": {
                    "index": 0
                }
            }
            ,
            "createItem": {
                "item": {
                    "title": "Qual o titulo do seu site?",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "textAnswers": {
                                "answers": [
                                    {
                                        "value": {
                                          "paragraph": True
                                        }
                                    }
                                ],
                                "shuffle": False
                            }
                        }
                    },
                },
                "location": {
                    "index": 1
                }
            },
            "createItem": {
                "item": {
                    "title": "Escolha uma cor para o seu site",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [
                                    {"value": "Azul"},
                                    {"value": "Cinza"},
                                    {"value": "Verde"},
                                    {"value": "Vermelho"},
                                    {"value": "Amarelo"},
                                    {"value": "Azul claro"},
                                    {"value": "Branco"},
                                    {"value": "Preto"}
                                ],
                                "shuffle": False
                            }
                        }
                    },
                },
                "location": {
                    "index": 2
                }
            },
            "createItem": {
                "item": {
                    "title": "Escolha a cor dos cartões de produtos do seu site",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [
                                    {"value": "Azul"},
                                    {"value": "Cinza"},
                                    {"value": "Verde"},
                                    {"value": "Vermelho"},
                                    {"value": "Amarelo"},
                                    {"value": "Azul claro"},
                                    {"value": "Branco"},
                                    {"value": "Preto"}
                                ],
                                "shuffle": False
                            }
                        }
                    },
                },
                "location": {
                    "index": 3
                }
            },
            "createItem": {
                "item": {
                    "title": "Escolha uma cor para os textos do seu site",
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [
                                    {"value": "Azul"},
                                    {"value": "Cinza"},
                                    {"value": "Verde"},
                                    {"value": "Vermelho"},
                                    {"value": "Amarelo"},
                                    {"value": "Azul claro"},
                                    {"value": "Branco"},
                                    {"value": "Preto"}
                                ],
                                "shuffle": False
                            }
                        }
                    },
                },
                "location": {
                    "index": 4
                }
            }
        }]
    }

    # Creates the initial form
    result = form_service.forms().create(body=NEW_FORM).execute()
    print(result["formId"])

    # Adds the question to the form
    question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()

    # Prints the result to show the question has been added
    get_result = form_service.forms().get(formId=result["formId"]).execute()
    print(get_result)


if __name__ == '__main__':
    generate()
