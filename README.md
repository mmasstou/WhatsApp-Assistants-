## Documentation du bot WhatsApp

### **Introduction**

Ce document décrit la création d'un bot WhatsApp en utilisant l'API Meta Cloud et Python, en particulier Flask. Nous intégrerons également des événements webhook pour recevoir des messages en temps réel et utiliserons OpenAI pour générer des réponses basées sur l'IA. Pour plus d'informations sur la structure de l'application Flask, veuillez consulter la documentation de Flask.

### **Prérequis**

* Un compte développeur Meta : Si vous n'en avez pas, vous pouvez en créer un ici : [https://developers.facebook.com/](https://developers.facebook.com/).
* Une application d'entreprise Meta : Si vous n'en avez pas, vous pouvez apprendre à en créer une ici : [https://www.facebook.com/business/help/1710077379203657](https://www.facebook.com/business/help/1710077379203657). Si vous ne voyez pas l'option de création d'une application d'entreprise, sélectionnez Autre > Suivant > Entreprise.

### **Structure du projet**

```
.
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── decorators
│   │   └── security.py
│   ├── models.py
│   ├── services
│   │   ├── __init__.py
│   │   └── openai_service.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
└── run.py
```

### **Partie Webhook**

Dans cette partie, nous allons créer un webhook pour écouter les réponses envoyées par l'API WhatsApp Messenger.

**Qu'est-ce qu'un webhook ?**

Un webhook peut être considéré comme un type d'API piloté par des événements plutôt que par des requêtes. Au lieu qu'une application demande à une autre de recevoir une réponse, un webhook est un service qui permet à un programme d'envoyer des données à un autre dès qu'un événement particulier se produit. Les webhooks sont simplement un moyen pour votre compte en ligne de s'écouter et de vous informer automatiquement sans que vous ayez à faire aucun effort.

**Ngrok**

Dans ce tutoriel, nous utiliserons ngrok comme webhook. Ngrok est un outil de tunneling populaire utilisé pour exposer une application locale en cours d'exécution sur Internet. Votre machine de développement peut être connectée à un réseau sécurisé derrière un pare-feu. Pour contourner les restrictions d'accès, ngrok exécute un petit processus client sur votre machine, créant un tunnel de connexion privé au service cloud. Votre serveur de développement localhost est mappé à un sous-domaine ngrok.io, auquel un utilisateur distant peut alors accéder. Il n'est pas nécessaire d'exposer les ports, de configurer le transfert de port ou d'apporter d'autres modifications au réseau.

Nous utiliserons donc ngrok pour exposer notre hôte local sur le Web et il nous fournira l'URL "https://" que nous pouvons utiliser pour recevoir la réponse du webhook.

### **Partie Flask App (écouteur API)**

Dans cette partie, nous allons créer un écouteur webhook en utilisant Flask, puis utiliser ngrok pour obtenir un lien "https://".

### **Partie LLM**

Dans cette partie, nous créerons un client OpenAI ChatGPT pour interagir et générer une réponse ou une action.

**Conclusion**

Ce document fournit une base pour la création d'un bot WhatsApp fonctionnel utilisant l'API Meta Cloud, Flask et OpenAI. N'hésitez pas à l'étendre et à l'adapter à vos besoins spécifiques.

### **Comment utiliser**

#### **Configuration de l'environnement de développement**

cree `.venv` and activate it :

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

intall re `requirements.txt`

```
pip install -r requirements.txt
```

then run app :

```
python run.py
```

#### **Configuration de ngrok :**

The steps below are taken from the [ngrok documentation](https://ngrok.com/docs/integrations/whatsapp/webhooks/).

You need a static ngrok domain because Meta validates your ngrok domain and certificate!

Once your app is running successfully on localhost, let's get it on the internet securely using ngrok!

1- If you're not an ngrok user yet, just sign up for ngrok for free.
2- Download the ngrok agent.
3- Go to the ngrok dashboard, click Your [Authtoken](https://dashboard.ngrok.com/get-started/your-authtoken), and copy your Authtoken.
4- Follow the instructions to authenticate your ngrok agent. You only have to do this once.
5- On the left menu, expand Cloud Edge and then click Domains.
6- On the Domains page, click + Create Domain or + New Domain. (here everyone can start with [one free domain](https://ngrok.com/blog-post/free-static-domains-ngrok-users))
7- Start ngrok by running the following command in a terminal on your local desktop:

```
ngrok http 8000 --domain your-domain.ngrok-free.app

```

8- ngrok will display a URL where your localhost application is exposed to the internet (copy this URL for use with Meta).







![1712142537953](images/README/1712142537953.png)
