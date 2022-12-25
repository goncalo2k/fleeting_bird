import tweepy
consumer_key = "7MV5r9wS3uotVhqIDH2xHFNBv"
consumer_secret = "Mc7G6mPekJigvVngN3W0wB9otSuKSILRFzopKsq6RYuG7nGaLR"
access_token = "1293329848216297474-SDbDJgdagzCppAJOA41X971ozsXkxD"
access_secret = "l7s1100173E5uTg9cVRaudFz5cDjaLSJKxnEDuU8SYo17"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPpGkwEAAAAAj0O88OHmd5n5wAbGlwHOC%2BqPoEs%3D2scC4XljokxIzm4teXFFFHZZ90FmgP3ICwBBxZUNoVNFiX5I2I"
client_id = "TlZidl9ZeWcwN3FUaXFOeGhtNXM6MTpjaQ"
client_secret = "o6UYgCDfOam-GZUN7a4bJ3bhZJkXMmXhSHl8jlZn7HYzuPHk2n"

client = tweepy.Client(bearer_token,consumer_key,consumer_secret,access_token,access_secret)
tweet = client.create_tweet(text="A testar tweepy :)")




