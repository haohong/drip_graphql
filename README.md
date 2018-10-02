# Drip graphql Code challenge

## Get started

### Install pyenv

Please reference [installation guide](https://github.com/pyenv/pyenv#installation)

### Install pipenv

Please reference [installation guide](https://pipenv.readthedocs.io/en/latest/install/)

### Get server running

```shell
$ git clone https://github.com/haohong/drip_graphql.git
$ cd drip_graphql
$ pipenv shell
$ pipenv install
$ ./manage.py runserver
```

## Query

Run the following query in [GraphiQL Playground](http://localhost:8000/graphql/)

```
query getPositions {
	positions {
		symbol
		quantity
		purchasePrice
		currentPrice
		marketValue
		portfolioPercent
		profitLoss
	}
}
```

## Mutation

Run the following query in [GraphiQL Playground](http://localhost:8000/graphql/)

```
mutation ProcessTrade {
	processTrades {
		positions {
			symbol,
			quantity,
			purchasePrice,
			currentPrice,
			marketValue,
			portfolioPercent,
			profitLoss,
		}
	}
}
```