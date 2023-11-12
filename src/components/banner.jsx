import Image from "next/image"
import Background from "../assets/images/background.jpg";

export default function Banner() {
  return (
    <div className="relative bg-gray-800 py-16 px-6 sm:py-20 sm:px-12 lg:px-16">
      <div className="absolute inset-0 overflow-hidden">
        <Image
          src={Background}
          alt=""
          className="w-full h-full object-center object-cover"
        />
      </div>

      <div
        aria-hidden="true"
        className="absolute inset-0 bg-gray-900 bg-opacity-50"
      />

      <div className="relative max-w-3xl mx-auto flex flex-col items-center text-center">
        <h2 className="my-8 text-3xl font-extrabold text-white sm:text-4xl">
          یک تجربه جدید!
        </h2>
      </div>
    </div>
  );
}
