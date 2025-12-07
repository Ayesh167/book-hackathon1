import React, {useState, useCallback, type ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Docusaurus Tutorial - 5min ⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  const [isChatbotOpen, setIsChatbotOpen] = useState(false);

  const toggleChatbot = useCallback(() => {
    setIsChatbotOpen(prev => !prev);
  }, []);

  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>

      {/* Floating Chatbot Button */}
      <button className={styles.chatbotButton} onClick={toggleChatbot} aria-label="Open chatbot">
        {isChatbotOpen ? '✕' : '💬'}
      </button>

      {/* Chatbot Window */}
      {isChatbotOpen && (
        <div className={styles.chatbotWindow}>
          <div className={styles.chatbotHeader}>
            <h3>How can I help you?</h3>
            <button className={styles.chatbotCloseButton} onClick={toggleChatbot} aria-label="Close chatbot">
              ✕
            </button>
          </div>
          <iframe
            src="http://localhost:8000/chatbot" // Placeholder URL, update as needed
            title="Chatbot"
            className={styles.chatbotIframe}
          ></iframe>
        </div>
      )}
    </Layout>
  );
}
