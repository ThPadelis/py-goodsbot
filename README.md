# Goodsbot
Goodsbot is a bot for dealing with daily deals from a Greek eshop.<br/>These deals come every day at 12pm Greece Time (or 10am UTC). In order to not visit their website every day and risk losing great deals due to lack of time or something, this bot will automatically notify you with a push notification at any device your set up.

## Prerequisites
1. [Python](https://www.python.org/) installed on your machine
2. [MongoDB](https://docs.mongodb.com/manual/installation/) installed on your machine or a [MongoDB Atlas](https://www.mongodb.com/) account
3. An account at [Pushbullet](https://www.pushbullet.com/) 
   1. Register
   2. Set up your devices (where you want to have your notifications)
   3. Go to Settings and Create Access Token
   4. Copy the token and paste it inside the `.env` file


## Usage

1. Clone the repository
    ```sh
    git clone https://github.com/ThPadelis/py-goodsbot.git
    ```
2. Install requirements
    ```sh
    pip install -r requirements.txt
    ```
3. Edit environment variables
    ```sh
    cp .env.example .env
    ```
4. Set up cronjob for daily notifications
    ```sh
    crontab -e 
    # add job
    TZ=UTC+2
    0 12 * * * path/to/python path/to/app.py
    ```

### Install requirements

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](./LICENSE)