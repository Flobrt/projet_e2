# Projet E2  

Le projet E2 vise à améliorer une application d'IA existante. Nous vous proposons ici une application permettant de prédire à partir d'une radio de cerveau la présence ou non d'une tumeur et le type de cette tumeur. Vous pouvez trouver plus de détails sur [le github de l'application originale](https://github.com/divine-architect/CNN-based-brain-tumor-diagnosis).  

Voici ce qui est attendu de vous :  

## Faire tourner l'application Flask telle qu'elle existe actuellement

Sur le [github de l'application originale](https://github.com/divine-architect/CNN-based-brain-tumor-diagnosis) vous pourrez trouver l'ensemble des dépendances dont vous avez besoin. Pas besoin de réentraîner le modèle, je l'ai fait pour vous et il est disponible sur ce dépôt. 

Vous pouvez déjà évaluer la qualité du modèle sur les données test utilisées par le développeur de manière plus approfondie (faire une matrice de confusion, proposer d'autres métriques que la seule accuracy). 

Une fois que votre application tourne, vous pouvez imaginer et coder une série de tests permettant de vérifier que l'application fonctionne correctement.  

## Améliorer l'application  

Vous le voyez, l'application est basique et tout tient sur une page html. Pour valider le E2, il vous faut intégrer une évolution fonctionnelle qui améliore le niveau de l'intelligence artificielle. Je vous propose plusieurs pistes :  

- Intégrer un modèle type YOLO permettant de segmenter sur l'image le lieu de la tumeur. Cela pourrait être fait dans un second temps, après la prédiction du modèle actuel, ou remplacer directement le modèle actuel. Il vous faudra trouver des données d'entraînement spécifiques à ce type de modèle, mais ça ne devrait pas être un trop gros problème.  

- Intégrer d'autres modèles de prédiction (poumons, coeur, ....) qui rendront l'application plus généraliste.  

Dans le cadre de l'implémentation, profitez-en pour améliorer l'aspect général de l'application : ajouter des onglets pour faire des nouvelles pages, permettre d'afficher l'image de la raido, etc...

En plus de l'amélioration de la partie IA, si vous avez le temps, vous pouvez en profiter pour changer le design de l'application, intégrer une authentification utilisateur, etc... À noter quand même que c'ets sur la partie IA que le jury vous attendra.  

## Tester votre nouvelle application  

On vous demande deux choses :  
- **Tester que l'application fonctionne au moins aussi bien qu'avant** (tests de régression). Les tests que vous avez implémentés à l'étape 1 tournent-ils bien toujours? 
- **Présenter les métriques d'évaluation de la nouvelle IA que vous avez intégrée**. Les comparer à l'ancien modèle, discuter d'en quoi vos modifications améliorent l'application.  

## Votre rapport  
le rapport doit faire de 5 à 10 pages. Soyez explicites avec des captures d'écran et des maquettes. Il faut que le jury voit à quoi ressemblait l'application avant et à quoi elle ressemble après, et comprenne ce que vous avez apporté. Présentez bien toutes les évaluations des modèles d'IA.
