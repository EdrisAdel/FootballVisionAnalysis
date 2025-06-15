import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './UI/index.css'
import App from './UI/App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
