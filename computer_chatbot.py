import spacy
from spacy.matcher import Matcher

# Charger le modèle français de spaCy
nlp = spacy.load("fr_core_news_sm")
matcher = Matcher(nlp.vocab)

# Définir les patterns pour les intentions
patterns = {
    "ORDINATEUR_LENT": [[{"LOWER": "lent"}], [{"LOWER": "ralenti"}], [{"LOWER": "ralentit"}]],
    "VIRUS": [[{"LOWER": "virus"}], [{"LOWER": "infecté"}], [{"LOWER": "pubs"}]],
    "ÉCRAN_NOIR": [[{"LOWER": "écran"}, {"LOWER": "noir"}], [{"LOWER": "rien"}, {"LOWER": "s'affiche"}]],
    "RÉSEAU": [[{"LOWER": "wifi"}], [{"LOWER": "internet"}], [{"LOWER": "réseau"}]],
    "PÉRIPHÉRIQUE": [[{"LOWER": "clavier"}], [{"LOWER": "souris"}], [{"LOWER": "imprimante"}]],
    "LOGICIEL_PLANTE": [[{"LOWER": "plante"}], [{"LOWER": "crash"}], [{"LOWER": "freeze"}]],
    "SALUTATION": [[{"LOWER": {"IN": ["bonjour", "salut", "coucou"]}}]],
    "REMERCIEMENT": [[{"LOWER": {"IN": ["merci", "thanks"]}}]],
    "AU_REVOIR": [[{"LOWER": {"IN": ["au", "revoir", "bye", "ciao"]}}]],
}

# Ajouter les patterns au matcher
for intent, pat in patterns.items():
    matcher.add(intent, pat)

# Générer une réponse selon l'intention
def generate_response(intent):
    responses = {
        "ORDINATEUR_LENT": "Essayez de redémarrer votre PC, désactiver les programmes au démarrage, et faire un scan antivirus.",
        "VIRUS": "Lancez un antivirus à jour (Windows Defender ou Malwarebytes) et évitez les sites non sécurisés.",
        "ÉCRAN_NOIR": "Vérifiez que le câble HDMI est bien branché. Essayez un autre écran ou port si nécessaire.",
        "RÉSEAU": "Redémarrez votre box internet. Assurez-vous que le wifi est activé sur l'ordinateur.",
        "PÉRIPHÉRIQUE": "Vérifiez les branchements. Essayez de reconnecter le périphérique ou tester sur un autre port USB.",
        "LOGICIEL_PLANTE": "Essayez de forcer la fermeture du logiciel et redémarrez l’ordinateur. Si le problème persiste, réinstallez l'application.",
        "SALUTATION": "Bonjour ! Décrivez-moi votre problème avec votre ordinateur.",
        "REMERCIEMENT": "Avec plaisir ! N'hésitez pas si vous avez d'autres questions.",
        "AU_REVOIR": "Merci d’avoir utilisé notre assistant. À bientôt !",
        "UNKNOWN": "Je n’ai pas compris votre problème. Pouvez-vous reformuler ou donner plus de détails ?"
    }
    return responses.get(intent, responses["UNKNOWN"])

# Boucle de conversation
print("Bot : Bonjour ! Je suis votre assistant de réparation d'ordinateur. Décrivez-moi votre problème.")
while True:
    message = input("Vous : ")
    if message.lower() in ["quit", "exit"]:
        print("Bot : Au revoir et bonne journée !")
        break

    doc = nlp(message)
    matches = matcher(doc)
    intent = nlp.vocab.strings[matches[0][0]] if matches else "UNKNOWN"
    print("Bot :", generate_response(intent))
