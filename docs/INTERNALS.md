# Αρχιτεκτονική Συστήματος

Η εφαρμογή που υλοποιήσαμε βασίζεται εξ ολοκλήρου στο [Django Web framework](http://djangoproject.com) και συγκεκριμένα
στις εκδόσεις >=1.2. 

Εξυπηρετώντας την αρχή [DRY](http://www.c2.com/cgi/wiki?DontRepeatYourself) και την επαναχρησιμοποίηση κώδικα,
η αρχιτεκτονική ενός Django project βασίζεται σε μεγάλο βαθμό στην ύπαρξη pluggable applications. Ένα application είναι 
ένα κομμάτι κώδικα που παρέχει μια συγκεκριμένη λειτουργία χωρίς λειτουργικές εξαρτήσεις από το υπόλοιπο project με σκοπό 
την εύκολη επαναχρησιμοποίησή του (με μικρές ίσως αλλαγές) και σε άλλα projects. 

Το Django ακολουθεί μια παραλλαγή του MVC (Model-View-Controller) design pattern που επιτρέπει το διαχωρισμό του 
business logic από την εμφάνιση/input και την αλληλεπίδραση με τη βάση δεδομένων.

## Views
Ένα view είναι μια απλή Python function που παίρνει από το Django ως parameter ένα HTTP request και εκτελεί την
κατάλληλη επεξεργασία πάνω σε αυτό. Επιστρέφει ένα HTTP response με τα αποτελέσματα της επεξεργασίας. "Ζουν" στο αρχείο
`views.py` μέσα σε κάθε app του project. Στο συγκεκριμένο project, η βασική λειτουργικότητα της εφαρμογής παρέχεται από
το app στο directory places/.

## URLs
Το Django μας επιτρέπει να σχεδιάσουμε τα URLs της εφαρμογής όπως εμείς θέλουμε, χωρίς κανέναν περιορισμό. Παρέχουμε
στον URL dispatcher μια αντιστοιχία (URLconf) μεταξύ URL patterns και των συναρτήσεων (views) που θα τα εξυπηρετούν και 
το Django αναλαμβάνει τα υπόλοιπα. Έτσι επιτυγχάνουμε κομψά, εύκολα και μόνιμα URLs όπως το "/articles/2003/03/3/" και
όχι σαν το "/articles.php?year=2003&month=03&day=3". Φυσικά, όπου έχει νόημα, μπορούμε να χρησιμοποιήσουμε και URLs με GET
parameters όπως τα παραπάνω. Στον κατάλογο του project υπάρχει το αρχείο με τα βασικά URLs (`src/estates/urls.py`) το
οποίο κάνει include τα επιμέρους URLs των διάφορων εφαρμογών.

## Templates
Η εμφάνιση της εφαρμογής καθορίζεται από τα templates (directory templates/). Ένα Django template δεν είναι τίποτα
περισσότερο από ένα HTML αρχείο που κάνει embed μια minimal python-like γλώσσα (Django template language) και γίνεται
render από το αντίστοιχο view. Στα templates υλοποιείται ουσιαστικά όλο το front-end κομμάτι της εφαρμογής. Βρίσκονται
στον κατάλογο `src/estates/templates`. Τα διάφορα στατικά αρχεία (css/javascript/images) βρίσκονται στο media/.

### Javascript/AJAX
Η εφαρμογή κάνει εκτενή χρήση JavaScript μέσω του πολύ διαδομένου framework [JQuery](jquery.com) σε διάφορα σημεία.
Πιο συγκεκριμένα, πέρα από τα απλά εφέ, χρησιμοποιείται για validation στην φόρμα εγγραφής, στην αναζήτηση, στην προβολή 
των φωτογραφιών και στη φόρμα προσθήκης νέας αγγελίας. Η αναζήτηση και το σύστημα "Αγαπημένων" βασίζονται σε AJAX requests.
AJAX χρησιμοποιείται επίσης και για τον έλεγχο ύπαρξης του username κατά την εγγραφή του χρήστη.

Τέλος, όλοι οι χάρτες της εφαρμογής δημιουργούνται με το Google Maps JavaScript API v3. Στην φόρμα δημιουργίας νέας αγγελίας,
το σύστημα προσπαθεί να εντοπίσει την ακριβή τοποθεσία του ακινήτου με geocoding από τα στοιχεία που εισήγαγε ο χρήστης.
Επειδή αυτό όμως δεν είναι κάτι που μπορεί να γίνεται πάντα με μεγάλη ακρίβεια δίνουμε τη δυνατότητα στο χρήστη να
"διορθώσει" την επιλογή του geocoder με το χέρι πάνω στο χάρτη. 

# Σχεδιασμός Βάσης

Όπως και στα περισσότερα Django projects, για την αλληλεπίδραση με τη βάση δεδομένων χρησιμοποιούμε το ORM 
(Object-Relational Mapper) του Django. Το ORM τακολουθεί το [Active Record design pattern](http://en.wikipedia.org/wiki/Active_record_pattern).
Ο ορισμός του schema γίνεται μέσω του Model API στο αρχείο `places/models.py`.

## Models
Ουσιαστικά, το ORM είναι ενα abstraction πάνω από το database API που μας επιτρέπει αλληλεπίδραση με τη βάση δεδομένων 
με κώδικα Python. Κάθε model δεν είναι τίποτα άλλο από μια κλάση η οποία εσωτερικά αναλαμβάνει τα SQL transactions με το
RDBMS.

Πιο συγκεκριμένα, διακρίνουμε τις εξής οντότητες:

* User: Αναπαριστά τον χρήστη.
* UserProfile: Επιπλέον στοιχεία του χρήστη (διεύθυνση, τηλέφωνο). Σχέση 1-1 με User.
* Place: Αναπαριστά το ακίνητο/αγγελία.
* Category: Κατηγορίες ακινήτων.
* Favorite: Συνδέει User-Place.
* Photo: Συνδέει φωτογραφίες με ακίνητα.
* Asset: Κάθε ακίνητο μπορεί να έχει κάποιες επιπλέον παροχές.

Κάθε μοντέλο αναπαρίσταται ως πίνακας στη βάση δεδομένων. Η δημιουργία της βάσης γίνεται μέσω του management utility
(`python manage.py syncdb`).

# Deployment

Το Django παρέχει έναν minimal application server, κυρίως για debugging της εφαρμογής, ο οποίος όμως δεν είναι κατάλληλος
για production deployment. Για αυτό το λόγο, το setup που θα χρησιμοποιήσουμε βασίζεται στον [nginx](nginx.net) και 
τον [uWSGI](http://projects.unbit.it/uwsgi/). Ο nginx είναι ένας από τους ταχύτερους web servers που κυκλοφορούν ενώ 
ο uWSGI είναι ένας πλήρης [WSGI](http://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) server. Ο nginx λαμβάνει 
τα requests στο port 80 και μέσω ενός unix socket τα προωθεί σε έναν (ή περισσότερους) uWSGI workers.

Για database server χρησιμοποιούμε PostgreSQL 8.4.

## Debug Server

Για να δοκιμάσουμε την εφαρμογή στον ενσωματωμένο server του Django αρκεί να τρέξουμε: 
    
    `python manage.py runserver 0.0.0.0:8000` 

στο root directory του project.

# Security

Το Djago, ως middleware, παρέχει στους προγραμματιστές όλα τα εργαλεία για τη δημιουργία ασφαλών web εφαρμογών.
Συγκεκριμένα, έχουμε μεριμνήσει για τα ακόλουθα ήδη επιθέσεων.

* SQL injection: Μια από τις βασικότερες αρχές στην ανάπτυξη web applications είναι το να μην εμπιστευόμαστε ποτέ 
user-submitted data και πάντα τα κάνουμε escape πριν τα χρησιμοποιήσουμε μέσα σε ένα SQL query. Το database API του Django
το αναλαμβάνει αυτό αυτόματα. Όλα τα SQL parameters γίνονται escape με βάση τους κανόνες κάθε database server (Postgres στο
συγκεκριμένο project).

* Cross-site Scripting (XSS): Απλή επίθεση που βασίζεται και πάλι σε non-sanitized URL parameters. Η λύση είναι απλή και
οι νέες εκδόσεις του Django την εφαρμόζουν από default: κάθε string που προέρχεται από το χρήστη πρέπει να γίνει escape.

* Cross-site Request Forgery (CSRF): Συμβαίνει όταν ένα κακόβουλο website εξαπατά το χρήστη φορτώνοντας/κάνοντας POST 
σε ένα URL από κάποιο άλλο website στο οποίο ο χρήστης είναι ήδη authenticated, εκμεταλλευόμενο έτσι το 
authentication status του χρήστη. Το Django παρέχει middleware για CSRF protection σε POST requests. Κάθε form που κάνει
POST έχει ένα hidden field με value κάποια κρυφή τιμή που γίνεται generate συνήθως από το session ID του χρήστη. Όταν
γίνεται η επεξεργασία της φόρμας (server-side) ελέγχουμε την τιμή του secret field και πετάμε error αν δεν κάνει 
validate.

# Internationalization

Για τη μετάφραση της εφαρμογής, το Django χρησιμοποιεί τη βιβλιοθήκη διεθνοποίησης gettext. Σε διάφορα σημεία μέσα στον
κώδικα μαρκάρουμε τα translation strings (είτε σε python code, είτε στα templates). Δίνοντας

    python manage.py makemessages -l el
    python manage.py makemessages -a

φτιάχνουμε το αρχείο μετάφρασης (`locale/el/LC_MESSAGES/django.po`). Αφού μεταφραστεί το αρχείο, δίνουμε
    
    python manage.py compilemessages

για να περαστούν οι αλλαγές στο Django.
