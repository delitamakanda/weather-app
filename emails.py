import weather
import mailer


def get_emails():
    emails = {}
    
    try:
        email_file = open('emails2.txt','r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
            
    except FileNotFoundError as err:
        print(err)


    return emails

def get_movies():
    try:
        movies = open('movies.txt', 'r')
        movie = movies.read()
    except FileNotFoundError as err:
        print(err)

    return movie

def get_pd():
    try:
        pds = open('liste_des_pd.txt', 'r')
        pds = pds.read()
    except FileNotFoundError as err:
        print(err)

    return pd

def main():
    emails = get_emails()
    print(emails)

    movie = get_movies()
    print(movie)
    
    pd = get_pd()
    print(pd)

    forcast = weather.get_weather_forcast()
    print(forcast)

    mailer.send_emails(emails, movie, pd, forcast)

main()
