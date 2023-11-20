import Head from "next/head";
import Header from "@/components/header";
import Banner from "@/components/banner";
import Tab from "@/components/tab";
import FoodCard from "@/components/foodcard";
import Footer from "@/components/footer";
import { ShoppingBagIcon } from "@heroicons/react/24/outline";

async function fetchMenuData() {
  const res = await fetch(
    "https://namya.ir/api/v1/businesses/798/restaurant"
  );

  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  const data = await res.json();
  const menu = data.data;
  return menu;
}

export default async function Home() {
  const menu = await fetchMenuData();
  return (
    <>
      <Head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <Header />
        <Banner />
        <Tab categories={menu} />

        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 sm:block">
          {menu.map((category, index) => (
            <div id={category.id} key={index}>
              <div  className="mt-12 flex-1 flex items-end justify-between">
                <h1 className="text-2xl font-bold text-gray-900">
                  {category.name}
                </h1>
                {index == 0 && (
                  <button className="border border-primary rounded-md py-2 px-6  flex items-center text-sm text-gray-700 space-x-2 space-x-reverse">
                    <ShoppingBagIcon className="flex-shrink-0 h-5 w-5 text-primary" />
                    <span className="text-sm text-primary">تکمیل خرید</span>
                  </button>
                )}
              </div>
              <div className="mt-6 grid grid-cols-1 lg:grid-cols-2  gap-6">
                {category.foods.map((food) => (
                  <FoodCard key={food.id} food={food} />
                ))}
              </div>
            </div>
          ))}
        </div>

        <Footer />
      </main>
    </>
  );
}
