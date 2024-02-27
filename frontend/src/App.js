import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios'
const base_url = 'http://localhost:5000'

function App() {

  const [coins, setCoins] = useState([])
  const [savedCoins, setSavedCoins] = useState([])
  const [missingCoins, setMissingCoins] = useState([]);
  const [refreshFlag, setRefreshFlag] = useState(false);

  const saveCoin = async (coin) => {
    axios.post('http://localhost:5000/add-coins', { name: coin.name, coin_id: coin.asset_id })
    setRefreshFlag(!refreshFlag);
  }

  useEffect(() => {
    fetch("http://localhost:5000/coins").then(
      response => {
        console.log(response)
        return response.json()
      }
    ).then(
      data => {
        console.log(data)
        setCoins(data)
        console.log(coins)
      }
    )

    fetch("http://localhost:5000/").then(
      response => {
        console.log(response)
        return response.json()
      }
    ).then(
      data => {
        console.log(data)
        setSavedCoins(data)
        console.log(savedCoins)
      }
    )
    
  }, [])

  useEffect(() => {
    const missingIds = savedCoins.reduce((missingIds, savedCoin) => {
      if (!coins.some(coin => coin.asset_id === savedCoin.coin_id)) {
        setMissingCoins(prev => [...prev, savedCoin.coin_id]); // Add the missing ID to the missingIds array
      }
      return missingIds;
    }, []);
    
  }, [savedCoins, coins]);
  
  useEffect(() => {
    console.log(missingCoins);
    console.log(`Missing Coins: ${missingCoins}`);
  }, [missingCoins]);
  

  return (
    <div className="App">
        <h1>Coins</h1>

        {coins.map((coin) => {
          return <div className={missingCoins.includes(coin.asset_id) ? 'saved' : 'coin'} key={coin.id_icon}><span>{coin.name}</span><button onClick={() => saveCoin(coin)}>Save</button></div>
        })}
    </div>
  );
}

export default App;
