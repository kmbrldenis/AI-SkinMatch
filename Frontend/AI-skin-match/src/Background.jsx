import backgroundvideo from "./assets/vecteezy_pastel-cosmetic-creams-in-glass-jars-against-orange-and_72001533.mp4"


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