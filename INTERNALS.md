# ~ Αρχιτεκτονική Συστήματος ~

Η εφαρμογή που υλοποιήσαμε βασίζεται εξ ολοκλήρου στο [Django Web framework](http://djangoproject.com) και συγκεκριμένα
στην έκδοση 1.2. Το Django ακολουθεί μια παραλλαγή του MVC (Model-View-Controller) design pattern που επιτρέπει το
διαχωρισμό του business logic από την εμφάνιση/input και την αλληλεπίδραση με τη βάση δεδομένων.

## ~ Views ~
Ένα view είναι μια απλή python function που παίρνει από το Django ως parameter ένα HTTP request και εκτελεί την
κατάλληλη επεξεργασία πάνω σε αυτό. Επιστρέφει ένα HTTP response με τα αποτελέσματα της επεξεργασίας.

## ~ URLs ~
Το Django μας επιτρέπει να σχεδιάσουμε τα URLs της εφαρμογής όπως εμείς θέλουμε, χωρίς κανέναν περιορισμό. Παρέχουμε
στον URL dispatcher μια αντιστοιχία (URLconf) μεταξύ URL patterns και των συναρτήσεων (views) που θα τα εξυπηρετούν και 
το Django αναλαμβάνει τα υπόλοιπα. Έτσι επιτυγχάνουμε κομψά, εύκολα και μόνιμα URLs όπως το "/articles/2003/03/3/" και
όχι σαν το "/articles.php?year=2003&month=03&day=3".

## ~ Templates ~
Η εμφάνιση της εφαρμογής καθορίζεται από τα templates (directory templates/). Ένα Django template δεν είναι τίποτα
περισσότερο από ένα HTML αρχείο που κάνει embed μια minimal python-like γλώσσα (Django template language) και γίνεται
render από το αντίστοιχο view.

# ~ Σχεδιασμός Βάσης ~

Όπως κάθε Django project, για την αλληλεπίδραση με τη βάση δεδομένων χρησιμοποιούμε το ORM (Object-relational mapping)
υποσύστημα του Django. Ο ορισμός του schema γίνεται μέσω του Model API στο αρχείο places/models.py.

Συγκεκριμένα, διακρίνουμε τις εξής οντότητες:

* User
* Place
* Category
* Favorite
* UserProfile

# ~ Deployment ~

PostgreSQL, nginx + uWSGI
