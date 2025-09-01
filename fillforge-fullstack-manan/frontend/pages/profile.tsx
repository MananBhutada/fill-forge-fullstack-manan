import { useState, useEffect } from 'react'
export default function Profile() {
  const [profile, setProfile] = useState(null)
  useEffect(()=>{
    fetch('/api/profile').then(r=>r.json()).then(setProfile).catch(()=>{})
  },[])
  return (<div style={{padding:20}}>
    <h2>Profile (placeholder)</h2>
    <pre>{JSON.stringify(profile,null,2)}</pre>
    <p>The frontend is scaffolded. Connect API calls to backend endpoints at http://localhost:8000</p>
  </div>)
}