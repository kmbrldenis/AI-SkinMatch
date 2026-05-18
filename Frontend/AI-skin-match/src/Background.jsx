import backgroundvideo from "./assets/vecteezy_a-facial-cleanser-some-flower-petals-placed-on-a-rock-next_51025826.mp4"

function Background () {
    return (
    <div className = "background">
        <video id = "video" autoPlay loop muted>
            <source src= {backgroundvideo} />
        </video>
    </div>
  )
}

export default Background