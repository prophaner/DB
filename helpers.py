import requests
import datetime

names = ['Liam', 'Emma', 'Noah', 'Olivia', 'William', 'Ava', 'James', 'Isabella', 'Logan', 'Sophia', 'Benjamin', 'Mia', 'Mason', 'Charlotte', 'Elijah', 'Amelia', 'Oliver', 'Evelyn', 'Jacob', 'Abigail', 'Lucas', 'Harper', 'Michael', 'Emily', 'Alexander', 'Elizabeth', 'Ethan', 'Avery', 'Daniel', 'Sofia', 'Matthew', 'Ella', 'Aiden', 'Madison', 'Henry', 'Scarlett', 'Joseph', 'Victoria', 'Jackson', 'Aria', 'Samuel', 'Grace', 'Sebastian', 'Chloe', 'David', 'Camila', 'Carter', 'Penelope', 'Wyatt', 'Riley', 'Jayden', 'Layla', 'John', 'Lillian', 'Owen', 'Nora', 'Dylan', 'Zoey', 'Luke', 'Mila', 'Gabriel', 'Aubrey', 'Anthony', 'Hannah', 'Isaac', 'Lily', 'Grayson', 'Addison', 'Jack', 'Eleanor', 'Julian', 'Natalie', 'Levi', 'Luna', 'Christopher', 'Savannah', 'Joshua', 'Brooklyn', 'Andrew', 'Leah', 'Lincoln', 'Zoe', 'Mateo', 'Stella', 'Ryan', 'Hazel', 'Jaxon', 'Ellie', 'Nathan', 'Paisley', 'Aaron', 'Audrey', 'Isaiah', 'Skylar', 'Thomas', 'Violet', 'Charles', 'Claire', 'Caleb', 'Bella', 'Josiah', 'Aurora', 'Christian', 'Lucy', 'Hunter', 'Anna', 'Eli', 'Samantha', 'Jonathan', 'Caroline', 'Connor', 'Genesis', 'Landon', 'Aaliyah', 'Adrian', 'Kennedy', 'Asher', 'Kinsley', 'Cameron', 'Allison', 'Leo', 'Maya', 'Theodore', 'Sarah', 'Jeremiah', 'Madelyn', 'Hudson', 'Adeline', 'Robert', 'Alexa', 'Easton', 'Ariana', 'Nolan', 'Elena', 'Nicholas', 'Gabriella', 'Ezra', 'Naomi', 'Colton', 'Alice', 'Angel', 'Sadie', 'Brayden', 'Hailey', 'Dominic', 'Emilia', 'Austin', 'Autumn', 'Ian', 'Quinn', 'Adam', 'Nevaeh', 'Elias', 'Piper', 'Jaxson', 'Ruby', 'Greyson', 'Serenity', 'Jose', 'Willow', 'Ezekiel', 'Everly', 'Carson', 'Cora', 'Evan', 'Kaylee', 'Maverick', 'Lydia', 'Bryson', 'Aubree', 'Jace', 'Arianna', 'Cooper', 'Eliana', 'Xavier', 'Peyton', 'Parker', 'Melanie', 'Roman', 'Gianna', 'Jason', 'Isabelle', 'Santiago', 'Julia', 'Chase', 'Valentina', 'Sawyer', 'Nova', 'Gavin', 'Clara', 'Leonardo', 'Vivian', 'Kayden', 'Reagan', 'Ayden', 'Mackenzie', 'Jameson', 'Madeline']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander']
registration_email = """
<head>
    <meta charset="UTF-8">
    <title>Verify your privacy</title>








  </head>

  <body style="margin: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; padding: 0; border-top: 2px solid #26334D; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: none; background-color: white; height: 100%; line-height: 1.6; width: 100%;">


  <meta name="viewport" content="width=device-width" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">
  <title style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">Privacy</title>



  <table class="body-wrap" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; width: 100%; background-color: white;">
    <tbody><tr style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">
      <td style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; vertical-align: top;"></td>
      <td class="container" style="font-size: 14px; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; padding: 0; line-height: 22px; vertical-align: top; margin: 0 auto; display: block; max-width: 400px; clear: both;" width="400">
        <div class="content" style="padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; margin: 0 auto; max-width: 400px; display: block;">
          <table class="main" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;" width="100%" cellspacing="0" cellpadding="0">
            <tbody><tr style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">
              <td class="logo" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; vertical-align: top; text-align: center;">
                <img src="https://privacy.com/assets/images/email/logo.png" style="padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; max-width: 100%; margin: 30px 0;" width="120">
              </td>
            </tr>
            <tr style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">
              <td class="content-wrap" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; vertical-align: top;">
                <table style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;" width="100%" cellspacing="0" cellpadding="0">
                  <tbody><tr style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">
                    <td class="content-block" style="font-size: 14px; margin: 0; box-sizing: border-box; line-height: 22px; vertical-align: top; color: #8F9BB3; padding: 20px 0; font-family: 'Helvetica Neue', Helvetica, Arial, 'Lucida Grande', sans-serif; background: #ffffff; border-radius: 3px; box-shadow: 0 0 0 1px #D8DDE2;">
                      <p style="margin: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; font-weight: normal; margin-bottom: 0; padding: 0 20px;"><strong style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; color: #596C80;">Please confirm your email address</strong>,
                        to activate your account. If you received this by mistake or weren't expecting it, please disregard this email.</p>
                    </td>
                  </tr>
                  <tr style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">
                    <td class="action" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; vertical-align: top; padding-top: 20px;">
                      <a href="127.0.0.1/registration/{payload}" class="btn-primary" style="line-height: 22px; margin: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #ffffff; font-size: 18px; padding: 20px; display: block; font-weight: bold; background: #00E056; border-radius: 3px; text-decoration: none; text-align: center;">Confirm email address</a>
                    </td>
                  </tr>
                </tbody></table>
              </td>
            </tr>
          </tbody></table>
        </div>
      </td>
    </tr>
  </tbody></table>
  <img src="http://ea.pstmrk.it/open/ODExOTBfMjU3MTYxX3ZlcmlmeS1lbWFpbF9lN2QyNzA0My03Mjk3LTQyYjUtODkzMC1lN2Y3M2M1ZjBlNDFfaGVsbG9AbWF0dGhld3NtaXRoLmNj" width="1" height="1" border="0">

<div class="footer" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; width: 100%; clear: both;">
  <table class="footer-table" style="margin: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px; padding: 40px 20px; background: white;" width="100%">
    <tbody><tr style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; color: #8F9BB3; font-size: 14px; line-height: 22px;">
      <td class="aligncenter content-block" style="margin: 0; box-sizing: border-box; line-height: 22px; vertical-align: top; padding: 20px 0; font-family: 'Helvetica Neue', Helvetica, Arial, 'Lucida Grande', sans-serif; color: #8F9BB3; text-align: center; font-size: 12px;">superid
        <a href="https://privacy.com" style="margin: 0; padding: 0; box-sizing: border-box; font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; line-height: 22px; color: inherit; font-size: 12px; text-decoration: none;">superid.com</a>
      </td>
    </tr>
  </tbody></table>
</div>







</body>"""


def send_email(email_address, token):
    api_key = "ab4196a0bb2bbef53b9f9f217842e124-2d27312c-e993c137"
    api_domain = "sandbox3ddc8e1d931c428fb340d1ad046d710c.mailgun.org"
    api_url = "https://api.mailgun.net/v3/{}/messages".format(api_domain)

    payload = {'token': token}

    auth = ('api', api_key)
    data = {"from": "Excited User <mailgun@{}>".format(api_domain),
            "to": email_address,
            "subject": "Email Registration",
            "html": registration_email.format(payload=payload)}

    sent = requests.post(api_url, auth=auth, data=data)
    return sent.raise_for_status()


def registration_expiration():
    now = datetime.datetime.utcnow()
    return now + datetime.timedelta(3)


