import React from 'react';
import './store.css';
import Card400 from '../../common/itemcard/card400';
const StoreHome = () => {
    return (
        <>
            <main className="storehome">
                {/*헤더*/}
                <div className="storehome_header">
                    <div className="storehome_header_left">
                        <div className="storehome_header_left_title">
                            스토어.좋아하는 Apple 제품을 구입하는 가장 좋은 방법.
                        </div>
                    </div>
                    <div className="storehome_header_right">
                        <section className="storehome_header_right_chat">
                            <div className="storehome_header_right_chat_img">
                                <img width="35" height="35" alt="" src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-chat-earth-day-specialist-icon-202504_AV4?wid=70&amp;hei=70&amp;fmt=jpeg&amp;qlt=90&amp;.v=MGlSYzZEcVYyWHpqdksxSCs4YjFLNzBQSmhWRTJPSGNQRHRFQ0RoYnJFNEtUTWVRaGpWVmhKOG83bW9wSUVGNXdpTHZxMWM3WWRmQnVUWUQ0V2tXSjdrNkxqcEdrM2x6OUZ3Z2JnTllhUU5XS0ZMbkg4ZVBxKzVXaGU3eFBVQnI"/>
                            </div>
                            <div className="storehome_header_right_chat_text_container">
                                <div className="storehome_header_right_chat_text">
                                    <p>쇼핑 지원이 필요하다면?</p>
                                </div>
                                <div className="storehome_header_right_chat_link">
                                <a href="#">스페셜리스트에게 문의하세요</a>
                                </div>
                            </div>
                        </section>
                        <section className="storehome_header_right_chat">
                            <div className="storehome_header_right_chat_img">
                                <svg width="25" height="35" viewBox="0 0 25 35" aria-hidden="true">
                                    <path d="m0 0h25v35h-25z" fill="none"></path>
                                    <path d="m12.4934 4.675a10.5617 10.5617 0 0 1 4.177.8275 10.8868 10.8868 0 0 1 5.7467 5.747 10.4988 10.4988 0 0 1 .8329 4.1777 10.3219 10.3219 0 0 1 -.6421 3.5951 10.8948 10.8948 0 0 1 -1.8669 3.2062 12.8406 12.8406 0 0 1 -2.9537 2.5775c-.984.6179-1.8226 1.1843-2.4931 1.6839a9.5187 9.5187 0 0 0 -1.7742 1.6788 6.8587 6.8587 0 0 0 -1.02 1.8034 6.8213 6.8213 0 0 0 -1.0278-1.8062 9.8247 9.8247 0 0 0 -1.7708-1.6742c-.6644-.4987-1.5014-1.0658-2.485-1.6834a12.5961 12.5961 0 0 1 -2.9617-2.5777 10.99 10.99 0 0 1 -1.8636-3.2083 10.3421 10.3421 0 0 1 -.6411-3.5951 10.5153 10.5153 0 0 1 .8319-4.1772 10.9669 10.9669 0 0 1 2.3209-3.4333 10.85 10.85 0 0 1 3.4278-2.3142 10.52 10.52 0 0 1 4.1628-.8275m0-1a11.4634 11.4634 0 0 0 -4.5561.9081 11.89 11.89 0 0 0 -6.2738 6.2709 11.4566 11.4566 0 0 0 -.9135 4.5732 11.2871 11.2871 0 0 0 .703 3.9416 11.9349 11.9349 0 0 0 2.0323 3.5006 13.5349 13.5349 0 0 0 3.1956 2.7835q1.446.9079 2.42 1.6384a8.7962 8.7962 0 0 1 1.5912 1.5 5.9225 5.9225 0 0 1 .9731 1.81q.25.7236.8285.7238t.8417-.7238a5.9779 5.9779 0 0 1 .967-1.81 8.4991 8.4991 0 0 1 1.59-1.5q.98-.73 2.4268-1.6384a13.7877 13.7877 0 0 0 3.19-2.7835 11.8367 11.8367 0 0 0 2.0373-3.5006 11.263 11.263 0 0 0 .7041-3.9416 11.44 11.44 0 0 0 -.9145-4.5732 11.8867 11.8867 0 0 0 -6.2717-6.2709 11.5044 11.5044 0 0 0 -4.57-.9081zm3.8566 9.71a2.3254 2.3254 0 0 0 -1.078 1.94 2.2152 2.2152 0 0 0 1.353 2.0506 4.7326 4.7326 0 0 1 -.693 1.4443c-.429.6174-.902 1.2458-1.584 1.2458-.693 0-.858-.4079-1.661-.4079-.77 0-1.045.4189-1.672.4189-.638 0-1.078-.5733-1.584-1.29a6.3114 6.3114 0 0 1 -1.056-3.3625 2.7185 2.7185 0 0 1 2.541-3.0208c.682 0 1.232.441 1.65.441.407 0 1.023-.4631 1.782-.4631a2.3483 2.3483 0 0 1 2.002 1.0036zm-3.729-1.1135c-.055 0-.099-.0111-.143-.0111 0-.033-.011-.11-.011-.1874a2.26 2.26 0 0 1 .561-1.3781 2.19 2.19 0 0 1 1.485-.7717 1.0735 1.0735 0 0 1 .011.1984 2.3284 2.3284 0 0 1 -.528 1.4222 1.9664 1.9664 0 0 1 -1.375.7276z"></path>
                            </svg>
                            </div>
                            <div className="storehome_header_right_chat_text_container">
                                <div className="storehome_header_right_chat_text">
                                    <p>Apple Store를 방문하세요</p>
                                </div>
                                <div className="storehome_header_right_chat_link">
                                    <a href="#">가까운 매장 찾기</a>
                                </div>
                            </div>
                        </section>
                    </div>
                </div>
                {/*스크롤 아이템*/}
                <div className="storehome_scroll_item">
                    <div className="storehome_scroll_item_container">
                        <div className="storehome_scroll_item_container_card_front"></div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-mac-nav-202503?wid=400&hei=260&fmt=png-alpha&.v=M1Q3OGxnb1lBaHhqNjZ2OVRXZmx4VEpBUDFBeEhMZS9GUnNSYXdEd0hscisrUlZaSVRoWVYzU0Qra0FoTmUwNng2bitObzZwQzk4cEorV1dZdzhIazVVcFlOTkdoMWg4ZkdDS1ovMUlzcW8"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">Mac</a>
                            </div>
                        </div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-iphone-nav-202502?wid=400&hei=260&fmt=png-alpha&.v=dW5XbHI1eDVpd01qWUU4bFRtWGZXOG9vbGw5MnhRZ3BpYVMwQTIvb2xsaDVoZlhhY1p4QWdsTjFNaGRHM3FYWW15d1FhSDJ0bkR0ZGZtUjZJNmFveFVockp1czQ4Q0pvWUU1bC9ERnl2dFE"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">
                                    <p>iPhone</p>
                                </a>
                            </div>
                        </div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-ipad-nav-202405?wid=400&hei=260&fmt=png-alpha&.v=dW5XbHI1eDVpd01qWUU4bFRtWGZXNGFLQTJVNnlNQmQrVmRBYnZYei9jckUzelNmMnRxajE0NHhmMWtLazl6eG53M0FRZHBXNTh1U1lFVEtSR2YzTm5qbE56RWRpRFNIRXZvbkd2S0l5dTg"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">
                                    <p>iPad</p>
                                </a>
                            </div>
                        </div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-watch-nav-202409?wid=400&hei=260&fmt=png-alpha&.v=S0tSVzBtSkRkSFFhMm1zS1NmeWtkNDJNVmlnVytwalkvOTJ2M1BKWUREdkh5NTJ6cGtEemJOblBHR043ZjFkZzAzOVFHb3N0MkVmS01ZcFh0d1Y4R2oxdUo4aWtyK05IRkZuWjBWbW5HM00"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">
                                    <p>Apple Watch</p>
                                </a>
                            </div>
                        </div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-vision-pro-nav-202401?wid=400&hei=260&fmt=png-alpha&.v=VzVpanYvTldHb05iVXFhc0xveWRLM25jd0w4dXFwc1hFbWZkNm9IcUR2bytSMWt1ZUNyTGx4SjRKL1pSL0ZDeGpCeVFkSWhuN0RJazJDeHBqaFFac0hlZzcwajlwb1R2dHNlazl1dldSUGQ5RzBLTDk5c25YRG5wR2ZpUlI4RFM"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">
                                    <p>Vision Pro</p>
                                </a>
                            </div>
                        </div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-airpods-nav-202409?wid=400&hei=260&fmt=png-alpha&.v=Q0Z1bWFqMUpRRnp3T0Y0VWJpdk1yNlJ5eGFhR1FVd2NNNDB0VWRUSzVCUFd1aTN5QlRYNG5PRjJxc2d1RklXbVM0TjRWdzF2UjRGVEY0c3dBQVZ6VFI0R1M4eFpKRTFIclV0ZHRqakVRd1k"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">
                                    <p>AirPods</p>
                                </a>
                            </div>
                        </div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-airtags-nav-202108?wid=400&hei=260&fmt=png-alpha&.v=Q0Z1bWFqMUpRRnp3T0Y0VWJpdk1ydzduWDk4YUM5R1JVL2gwcEZnWWNaRFd1aTN5QlRYNG5PRjJxc2d1RklXbVM0TjRWdzF2UjRGVEY0c3dBQVZ6VFpQclc0OVE3cmhmS3FBaXd6cG8yYzg"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">
                                    <p>AirTags</p>
                                </a>
                            </div>
                        </div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-appletv-nav-202210?wid=400&hei=260&fmt=png-alpha&.v=T0wvM1N3YUcxQ09qK0VNRkl1RU1BZFM5WnN0RmVZRmVXQ0FCUWJjbnJDald1aTN5QlRYNG5PRjJxc2d1RklXbVM0TjRWdzF2UjRGVEY0c3dBQVZ6VFZ3YmJrVi9SakQxWUcrYWQwVXc5VTA"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">
                                    <p>Apple TV 4K</p>
                                </a>
                            </div>
                        </div>
                        <div className="storehome_scroll_item_container_card">
                            <div className="storehome_scroll_item_container_img">
                                <img src="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-13-accessories-nav-202503?wid=400&hei=260&fmt=png-alpha&.v=QnhsNk96S0o4R1dkN2FveStNM1hwNzZGMHVrNGw2NTM5Vmk2bHZzMXQ3aUJGVHdnWkxMaklDeW9JYU5tT3FWeVBrcjVFNVdueFRVbVY3TGtiL2RjUVhQYS92MS9scmN4eTZLbFFkMHVzTVhuL2FLN3hwSUJhbzdFUHltVU1ldnQ"/>
                            </div>
                            <div className="storehome_scroll_item_container_img_text">
                                <a href="#">
                                    <p>액세서리</p>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                {/*최신 제품 소개*/}
                <div className="storehome_latest_product">
                    <Card400 product_name="iPhone 16" product_text="iPhone 16 라인업을 만나볼까요?" product_price="100,000원" product_image="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/store-card-40-macbook-air-202503?wid=800&hei=1000&fmt=p-jpg&qlt=95&.v=MjhMcWJ2MGZwbXEwdnBkcUN6ZnhyOWVOMytmanI1M0ZTQWR1RjlDMWJpNXFTRjNxbmh1UnU2R29ibGdpZUFXc0prY3crUWRsN1dqVjRnMHR5S1hVbk15N0N0R0lhUGhlMG1Tdmc3RjZVQ09NTUhYNlZ6OGxKNWpBMHlTSTlldko"/>
                </div>
                

            </main>
        </>
    );
};

export default StoreHome;