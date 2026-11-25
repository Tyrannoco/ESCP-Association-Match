class Association :
  def __init__(self,categorie,nom,investissement,cotisation,taille,experience_pro,voyage,diversite_internationale) :
    self.categorie = categorie
    self.nom = nom
    self.investissement = investissement
    self.cotisation = cotisation
    self.taille = taille
    self.experience_pro = experience_pro
    self.voyage = voyage
    self.diversite_internationale = diversite_internationale


junior_entreprise = Association("professionnelle","junior entreprise","fort","fort","grand","fort","oui","non")
bde = Association("vie de campus","bureau des élèves","fort","fort","grand","fort","non","non")
deliscep = Association("vie de campus","DELISCEP","moyen","faible","grand","faible","non","non")
streams = Association("vie de campus","STREAMS","faible","faible","petit","faible","non","non")
shuffle = Association("vie de campus","SHUFFLE","moyen","faible","moyen","faible","non","oui")
scepi = Association("vie de campus","SCEPI","moyen","faible","grand","faible","non","oui")
quatter = Association("vie de campus","QUATTER","fort","moyen","moyen","moyen","non","non")
par_idylle = Association("vie de campus", "Par'idylle","faible","moyen","moyen","faible","non","non")
artmaniac = Association("artistique","Art Maniac","fort","fort","grand","faible","non","non")
bda = Association("artistique","Bureau Des Arts","moyen","faible","petit","faible","non","non")
lifeshot = Association("artistique","Life Shot","moyen","faible","petit","non","non","non")
vo = Association("artistique","Version Originale","moyen","faible","petit","non","non","non")
runaway = Association("artistique","Runaway","moyen","faible","moyen","non","non","non")
comu = Association("musique","CoMu","fort","moyen","grand","fort","non","non")
underscep = Association("musique","underscep","moyen","moyen","petit","non","non","non")
on_air = Association("musique","On Air","moyen","moyen","grand","non","non","non")
polyphony = Association("musique","Polyphony","moyen","moyen","moyen","non","non","non")
latinascep = Association("culturelle","Latinascep","moyen","faible","moyen","non","non","oui")
escp_algeria = Association("culturelle","ESCP Algeria","faible","faible","petit","non","non","oui")
escp_liban = Association("culturelle","ESCP Liban","faible","faible","petit","non","non","oui")
amicale = Association("culturelle","amicale","moyen","faible","moyen","non","non","non")
communaute_chretienne = Association("culturelle","Communauté Chrétienne","faible","faible","petit","non","non","non")
communaute_musulmane = Association("culturelle","Communauté Musulmane","faible","faible","petit","non","non","non")
escp_israel = Association("culturelle","ESCP Israel","faible","faible","petit","non","non","oui")
chas_scep_esh = Association("culturelle","Chas'scep'esh","moyen","moyen","moyen","non","non","non")
scep_asia = Association("culturelle","SCEP asia","moyen","faible","moyen","non","non","oui")
afroscep = Association("culturelle","Afroscep","fort","faible","grand","faible","oui","non")
escp_maroc = Association("culturelle","ESCP Maroc","faible","non","petit","non","oui","oui")
cheer_up = Association("humanitaire","Cheer'up","fort","faible","grand","non","non","non")
rudez = Association("humanitaire","Rudez","fort","fort","moyen","non","oui","oui")
solidarite_france_nepal = Association("humanitaire","Solidarité France Népal","fort","fort","grand","non","oui","oui")
fleur_de_bitume = Association("humanitaire","Fleur de Bitume","moyen","faible","moyen","oui","non","oui")
era = Association("humanitaire","ERA","fort","faible","moyen","oui","non","oui")
aware = Association("société","Aware","moyen","faible","moyen","non","non","non")
escape = Association("société","Escape","faible","faible","petit","non","non","non")
noise = Association("société","Noise","moyen","faible","moyen","oui","non","non")
ski_club = Association("sportive", "Ski Club / Skloub","moyen","fort","grand","moyen","oui","non")
star_trekk = Association("sportive", "Star Trekk' ESCP","fort","moyen","grand","moyen","non","non")
turbo_scep = Association("sportive", "Turbo SCEP / Automobile Club ESCP","faible","moyen","petit","faible","non","non")
yachting_club = Association("sportive", "Yachting Club","faible","moyen","moyen","faible","oui","non")
challenge = Association("professionnelle", "ESCP Challenge", "fort", "fort", "grand","fort", "oui", "non")
leconomique = Association("professionnelle", "L'Économique ESCP", "faible", "faible", "petit","fort", "non", "oui")
escp_ai = Association("professionnelle", "ESCP AI Society", "faible", "faible", "petit","fort", "non", "oui")
escprit_defense = Association("professionnelle", "ESCPRIT Défense", "moyen", "faible", "petit","fort", "non", "oui")
escpression = Association("professionnelle", "ESCP'ression", "faible", "faible", "petit","fort", "non", "non")
le_cercle = Association("professionnelle", "Le Cercle ESCP", "fort", "faible", "petit","fort", "non", "oui")
bds = Association("sportive", "BDS", "moyen", "faible", "grand","moyen", "non", "non")
budse = Association("sportive", "BUDSE", "fort", "fort", "moyen","fort", "oui", "non")

associations = [
    junior_entreprise, bde, deliscep, streams, shuffle,
    scepi, quatter, par_idylle, artmaniac, bda,
    lifeshot, vo, runaway, comu, underscep,
    on_air, polyphony, latinascep, escp_algeria,
    escp_liban, amicale, communaute_chretienne,
    communaute_musulmane, escp_israel, chas_scep_esh,
    scep_asia, afroscep, escp_maroc, cheer_up,
    rudez, solidarite_france_nepal, fleur_de_bitume,
    era, aware, escape, noise, ski_club,
    star_trekk, turbo_scep, yachting_club,
    challenge, leconomique, escp_ai,
    escprit_defense, escpression, le_cercle,
    bds, budse
]

poids = {
    "categorie": 5,
    "investissement": 1,
    "cotisation": 1,
    "taille": 1,
    "experience_pro": 0.5,
    "voyage": 1,
    "diversite_internationale": 0.5
}

class Utilisateur :
  def __init__(self,categorie,investissement,cotisation,taille,experience_pro,voyage,diversite_internationale):
    self.categorie = categorie
    self.investissement = investissement
    self.cotisation = cotisation
    self.taille = taille
    self.experience_pro = experience_pro
    self.voyage = voyage
    self.diversite_internationale = diversite_internationale

def demander_reponse(question, choix_valides):

    while True:

        reponse = input(question).strip().lower()

        if reponse in choix_valides:
            return reponse

        print("Réponse invalide.")
        print("Choix possibles :", choix_valides)

def matching(utilisateur, associations):

    meilleur_score = -1
    meilleure_association = None

    for i in range(len(associations)):

        score = 0

        if associations[i].categorie == utilisateur.categorie:
            score += poids["categorie"]

        if associations[i].investissement == utilisateur.investissement:
            score += poids["categorie"]

        if associations[i].cotisation == utilisateur.cotisation:
            score += poids["categorie"]

        if associations[i].taille == utilisateur.taille:
            score += poids["categorie"]

        if associations[i].experience_pro == utilisateur.experience_pro:
            score += poids["categorie"]

        if associations[i].voyage == utilisateur.voyage:
            score += poids["categorie"]

        if associations[i].diversite_internationale == utilisateur.diversite_internationale:
            score += poids["categorie"]

        if score > meilleur_score:
            meilleur_score = score
            meilleure_association = associations[i]

    return meilleure_association, meilleur_score

def creer_utilisateur():

    investissement = demander_reponse("Investissement (faible/moyen/fort) : ",["faible", "moyen", "fort"])
    voyage = demander_reponse("Voyage (oui/non) : ",["oui", "non"])
    categorie = demander_reponse("Catégorie : (professionnelle, musique, société, culinaire) ", [ "professionnelle",
    "vie de campus",
    "artistique",
    "musique",
    "culturelle",
    "humanitaire",
    "société",
    "sportive"])
    cotisation = demander_reponse("Cotisation (faible, moyen, fort) : ",["faible","moyen","fort"])
    taille = demander_reponse("Taille (grand, petit, moyen): ", ["grand", "petit","moyen"])
    experience_pro = demander_reponse("Expérience professionnelle (fort, moyen, faible):", ["fort","moyen","faible"])
    diversite = demander_reponse("Diversité internationale (oui,non)",["oui","non"])

    return Utilisateur(
        categorie,
        investissement,
        cotisation,
        taille,
        experience_pro,
        voyage,
        diversite
    )
# Création d'un utilisateur
utilisateur1 = creer_utilisateur()

# Recherche de la meilleure association
association, score = matching(utilisateur1, associations)

# Affichage du résultat
score_max = sum(poids.values())
pourcentage = (score / score_max) * 100

print("Compatibilité :", pourcentage, "%")
print("L'association qui vous correspond le mieux est :", association.nom)
print("Votre score de compatibilité est :", pourcentage, "%")
