import Link from 'next/link'
export default function Home() {
  return (
    <main style={{padding:20}}>
      <h1>FillForge Auto - Demo Frontend</h1>
      <p>This is a scaffolded frontend. Use the backend at http://localhost:8000</p>
      <ul>
        <li><Link href='/profile'>Profile</Link></li>
        <li><Link href='/documents'>Documents</Link></li>
        <li><Link href='/forms'>Forms</Link></li>
      </ul>
    </main>
  )
}